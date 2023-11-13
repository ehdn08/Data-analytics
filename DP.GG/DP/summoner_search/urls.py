from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_summoner, name='search_summoner'),
    
]