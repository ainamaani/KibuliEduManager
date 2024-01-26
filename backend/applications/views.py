from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError as DjangoValidationError

from django.shortcuts import render,get_object_or_404
from itertools import cycle
import random
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from datetime import date, timedelta, datetime
from . models import Application
from . serializers import ApplicationSerializer
from students.models import Student

# Create your views here.
class ApplicationList(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request , *args, **kwargs):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            # custom validation before saving
            if self.custom_validation(serializer.validated_data, request.FILES):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({ 'error': 'Custom validation failed' }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def custom_validation(self, validated_data,files):

        for field_name in ['recommendation_letter','passport_photo','results_document']:
            if field_name in files:
                file = files[field_name]
                try:
                    FileExtensionValidator(allowed_extensions=['pdf','jpeg','jpg','png','doc','docx'])(file)
                except DjangoValidationError as e:
                    raise ValidationError({"file": [str(e)]})
        
        # Check if date of birth is not a future date and at least 10 years in the past
        if 'date_of_birth' in validated_data:
            today = date.today()
            age_limit_date = today - timedelta(days=365*10) #ten years in days
            if validated_data['date_of_birth'] > today:
                raise ValidationError({ 'date_of_birth':["The date of birth can't be a future date"]})
            elif validated_data['date_of_birth'] < age_limit_date:
                raise ValidationError({ 'date_of_birth':["You must be at least 10 years old"] })
            
        return True
            

    def get(self, request):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        application = get_object_or_404(Application, pk=pk)
        application.delete()
        return Response({ 'message':'Application deleted successfully' })
    
    def put(self, request, pk):
        application_to_update = get_object_or_404(Application, pk=pk)
        serializer = ApplicationSerializer(application_to_update,data=request.data,partial=True)

        if serializer.is_valid():
            # custom validation before saving
            if self.custom_validation(serializer.validated_data):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({ 'error': 'Custom validation failed' }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApplicationDetail(APIView):
    def get(self,request,pk):
        application = get_object_or_404(Application, pk=pk)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)


# function to accept the application
def accept_application(self,request,pk):
    application_to_accept = get_object_or_404(Application, pk=pk)
    application_to_accept.application_status = 'accepted'
    # save the modified object
    application_to_accept.save()

    # create new student after acceptance of the application

    # list of houses
    houses = ['africa','agarkhan','kakungulu','luwangula']
    # get number of already created students
    num_students = Student.objects.count()
    # determine the index of the house to be allocated based on the number
    house_index = num_students % len(houses)

    # allocation of clubs
    clubs = cycle(['interact','rotery','aids','nkobazambogo','kmsa'])
    # use the next function to get the next club in the cycle
    club_to_assign = next(clubs)

    # handle the student number allocation for the newly created student
    # get current year
    current_year = datetime.now().year % 100
    std_number = f"{current_year:02d}-{num_students + 1:03d}"


    # handle the allocation of streams
    if application_to_accept.class_applied_for in ['F1','F2','F3','F4']:
        streams = ['F1','F2','F3','F4']
        # Shuffle the list of streams to randomize the allocation
        random.shuffle(streams)
        # Use the next function to get the next stream in the shuffled list
        assigned_stream = next(iter(streams))
    

    new_student = Student.objects.create(
        first_name=application_to_accept.first_name,last_name=application_to_accept.last_name,
        email=application_to_accept.email,phone_number=application_to_accept.phone_number,
        profile_pic=application_to_accept.passport_photo,guardian=application_to_accept.guardian_name,
        guardian_email=application_to_accept.guardian_email,guardian_phone_number=application_to_accept.guardian_phone_number,
        relationship_with_guardian=application_to_accept.relationship_with_guardian,
        current_class=application_to_accept.class_applied_for, religion=application_to_accept.religion,
        gender=application_to_accept.gender,date_of_birth=application_to_accept.date_of_birth,
        date_joined=datetime.now(),combination=application_to_accept.combination_applied_for,
        disabled=application_to_accept.disabled,disabled_description=application_to_accept.disabled_description,
        any_chronic_disease_condition=application_to_accept.any_chronic_disease_condition,
        chronic_disease_condition_description=application_to_accept.chronic_disease_condition_description,
        house=houses[house_index],club=club_to_assign,student_number=std_number,stream=assigned_stream
    )
    new_student.save()


    # Send email to the applicant after accepting the application
    subject = 'Application Accepted'
    message = render_to_string('application_accepted_email.html', {
        'applicant_name': application_to_accept.first_name,
        'student_number': new_student.student_number,
        'house': new_student.house,
        'club': new_student.club
        # You can add more variables here based on your email template
    })
    plain_message = strip_tags(message)  # Strip HTML tags for the plain text version
    from_email = 'aina.isaac2002@gmail.com'  
    to_email = application_to_accept.email

    send_mail(subject, plain_message, from_email, [to_email], html_message=message)

@api_view(['GET'])
def reject_application(request,pk):
    application_to_reject = get_object_or_404(Application, pk=pk)
    # change the application status to rejected
    application_to_reject.application_status = "rejected"
    # save the updated object
    application_to_reject.save()

    # Send email to the applicant after accepting the application
    subject = 'Application Rejected'
    message = render_to_string('application_rejected_email.html',{
        'applicant_name' : application_to_reject.first_name
    })
      
    
    plain_message = strip_tags(message)  # Strip HTML tags for the plain text version
    from_email = 'aina.isaac2002@gmail.com'  
    to_email = application_to_reject.email

    send_mail(subject, plain_message, from_email, [to_email], html_message=message)

    # Return a JSON response with the appropriate renderer
    return Response({'message': 'Application rejected successfully'}, status=status.HTTP_200_OK)

