from django.urls import path, include
from . import views
from .views import BookViewSet#, Another
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('first', views.first), # views.first is a function call from this folder's views.py
    # path('another', Another.as_view()),
]
