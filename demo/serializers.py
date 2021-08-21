from rest_framework import serializers
from .models import Book

# This is what decides what is returned when requesting a certain url
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'published', 'id']