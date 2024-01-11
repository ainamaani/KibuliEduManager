from django.shortcuts import render, get_object_or_404
from . serializers import BookSerializer
from . models import Book
from datetime import datetime, date
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

# Create your views here.
class BookList(APIView):
    def post (self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            # custom validation before saving
            if self.custom_validation(serializer.validated_data):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({ 'error': 'Custom validation failed' }, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def custom_validation(self, validated_data):
        # check if all required fields have been provided
        required_fields = [
            'title','isbn','author','publisher','number_of_pages',
            'description','publication_date','category','language','edition','number_of_copies'
        ]

        for field in required_fields:
            if field not in validated_data:
                raise ValidationError({ 'required':["Please fill in all the required field"]})
            
        # check if the ISBN is atleast 10 characters
        if 'isbn' in validated_data and len(validated_data['isbn']) < 10:
            raise ValidationError({'isbn': ["ISBN can't be less than 10 digits, enter a valid code"]})

        # check if the publication date is not a future date
        if 'publication_date' in validated_data and validated_data['publication_date'] > date.today():
            raise ValidationError({'publication_date': ["The publication date can't be future date "]})
        

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        book = get_object_or_404 (Book, pk=pk)
        book.delete()
        return Response({'message':'Book deleted successfully'}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        book_to_update = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            # custom validation before saving
            if self.custom_validation(serializer.validated_data):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({ 'error': 'Custom validation failed' }, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookDetail(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
