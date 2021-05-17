from django.urls import path
from . import views

urlpatterns = [
    path('', views.contents, name='contents'),
    path('<int:content_id>', views.content, name='content'),
    path('search/', views.search, name='search'),
    path('tag/<slug:slug>/', views.tagged, name='tagged'),
]