from django.shortcuts import render, get_object_or_404
from rest_framework import status
from datetime import date,datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from . serializers import StudentSerializer
from . models import Student

# Create your views here.
class StudentList(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            # do custom validation before saving the database
            if self.custom_validation(serializer.validated_data):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({ 'error': 'Custom validation failed'}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def custom_validation(self, validated_data):
        # check if all the required fields have been provided
        required_fields = [
            'first_name','last_name','email','phone_number','profile_pic','guardian',
            'guardian_email','guardian_phone_number','house','club','current_class','stream',
            'religion','gender','student_number','date_of_birth','date_joined',
            'combination','disabled','any_chronic_disease_condition'
        ]

        for field in required_fields:
            if field not in validated_data:
                raise ValueError({ 'required':["All fields are required"] })
            
        if 'phone_number' in validated_data and len(validated_data['phone_number']) < 10:
            raise ValidationError({ 'phone_number':["Please supply a valid phone number"] })
        
        if 'guardian_phone_number' in validated_data and len(validated_data['guardian_phone_number']) < 10:
            raise ValidationError({ 'guardian_phone_number':["Please supply a valid guardian phone number"] })
        
        if 'house' in validated_data and validated_data['house'] not in ['africa','agarkhan','kakunguru','luwangula']:
            raise ValidationError({ 'house':["The house must be one of 'Africa','Agarkhan','Kakunguru' or 'Luwangula'"] })
        
        if 'current_class' in validated_data and validated_data['current_class'] not in ['F1','F2','F3','F4','F5','F6']:
            raise ValidationError({ 'current_class':["The current class has to one of 'F1','F2','F3','F4','F5' or 'F6'"] })
        
        if 'gender' in validated_data and validated_data['gender'] not in ['male','female']:
            raise ValidationError({ 'gender':["The gender must be 'male' or 'female'"] })
        
        if 'religion' in validated_data and validated_data['religion'] not in ['christianity','islam']:
            raise ValidationError({ 'religion':["The religion must be 'christianity' or 'islam'"] })


    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response({'message': 'Student deleted successfully'}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            # do custom validation before saving the database
            if self.custom_validation(serializer.validated_data):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({ 'error': 'Custom validation failed'}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetail(APIView):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    

def change_student_status(self, request, student_number):
    student_to_change_status = Student.objects.get(student_number=student_number)
    if student_to_change_status.status == 'activate':
        student_to_change_status.status == 'inactive'
    else:
        student_to_change_status == 'active'

    student_to_change_status.save()


def handle_student_leaving(self, request, student_number):
    student_left = Student.objects.get(student_number=student_number)
    student_left.status = 'inactive'
    student_left.date_left = datetime.now()
    student_left.save()

