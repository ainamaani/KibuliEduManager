from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import status
from datetime import date, timedelta
from . models import Application
from . serializers import ApplicationSerializer

# Create your views here.
class ApplicationList(APIView):
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            # custom validation before saving
            if self.custom_validation(serializer.validated_data):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({ 'error': 'Custom validation failed' }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def custom_validation(self, validated_data):
        #check if all required fields are provided
        required_fields = [
                            'first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number',
                            'address', 'current_class', 'school', 'school_location', 'school_phone_number',
                            'change_reason', 'class_applied_for', 'passport_photo',
                            'results_document', 'guardian_name', 'guardian_phone_number', 'relationship_with_guardian'
                           ]
        for field in required_fields:
            if field not in validated_data:
                raise ValidationError({ 'required':["Please fill in all the required fields"]})
            
        #check if the phone number is greater than 10 digits
        if 'phone_number' in validated_data and len(validated_data['phone_number']) < 10:
            raise ValidationError({ 'phone_number':["The phone number must be greater than 10 digits"]})
        
        #check if the school phone number is greater than 10 digits
        if 'school_phone_number' in validated_data and len(validated_data['school_phone_number']) < 10:
            raise ValidationError({ 'school_phone_number':["The school phone number must be greater than 10 digits"]})
        
        #check if the school phone number is greater than 10 digits
        if 'guardian_phone_number' in validated_data and len(validated_data['guardian_phone_number']) < 10:
            raise ValidationError({ 'guardian_phone_number':["The guardian phone number must be greater than 10 digits"]})
        
        #check if gender is one of the provided options
        if 'gender' in validated_data and validated_data['gender'] not in ['male', 'female']:
            raise ValidationError({ 'gender':["The gender must be either 'male' or 'female'"]})
        
        # Check if date of birth is not a future date and at least 10 years in the past
        if 'date_of_birth' in validated_data:
            today = date.today()
            age_limit_date = today - timedelta(days=365*10) #ten years in days
            if validated_data['date_of_birth'] > today:
                raise ValidationError({ 'date_of_birth':["The date of birth can't be a future date"]})
            elif validated_data['date_of_birth'] < age_limit_date:
                raise ValidationError({ 'date_of_birth':["You must be at least 10 years old"] })

    def get(self, request):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
    
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