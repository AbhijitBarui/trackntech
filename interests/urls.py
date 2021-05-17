from django.urls import path
from . import views

urlpatterns = [
    path('interest', views.interest, name='interest'),
]