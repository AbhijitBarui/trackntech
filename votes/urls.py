from django.urls import path
from . import views

urlpatterns = [
    path('upvote', views.upvote, name='upvote'),
    path('downvote', views.downvote, name='downvote'),
]