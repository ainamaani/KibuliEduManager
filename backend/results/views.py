from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import ResultsSerializer
from . models import Result

# Create your views here.

class ResultsList(APIView):
    def get(self, request):
        results = Result.objects.all()
        serializer = ResultsSerializer(results, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ResultsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

    def calculate_grades(self, validated_data):
        if validated_data['mark'] < 40:
            validated_data['grade'] = 'F9'
        elif 40 <= validated_data['mark'] < 45:
            validated_data['grade'] = 'P8'
        elif 45 <= validated_data['mark'] < 50:
            validated_data['grade'] = 'P7'
        elif 50 <= validated_data['mark'] < 55:
            validated_data['grade'] = 'C6'
        elif 55 <= validated_data['mark'] < 60:
            validated_data['grade'] = 'C5'
        elif 60 <= validated_data['mark'] < 65:
            validated_data['grade'] = 'C4'
        elif 65 <= validated_data['mark'] < 74:
            validated_data['grade'] = 'C3'
        elif 75 <= validated_data['mark'] < 79:
            validated_data['grade'] = 'D2'
        else:
            validated_data['grade'] = 'D2'
        