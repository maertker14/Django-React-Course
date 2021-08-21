from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets # for serializers
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,) # how we restrict access to only people who recieve a token from us (How to create token in code?)
    permission_classes = (IsAdminUser,) # can also do IsAdminUser


# class Another(View):
#     books = Book.objects.all() # give me all the objects in the Book database
#     output = ''
#     for book in books:
#         output += f"We have {book.title} book in the DB with id: {book.id}<br>"
#
#     def get(self, request):
#         return HttpResponse(self.output)
#
#
def first(request):
    return render(request, 'first_temp.html', {'data': 'this is from views'})
