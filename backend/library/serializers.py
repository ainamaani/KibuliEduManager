from rest_framework import serializers
from . models import Book,TakenBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class TakenBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakenBook
        fields = '__all__'