from django.urls import path
from .views import  registerview


urlpatterns = [
    
    path('', registerview.as_view() , name=' register'),
  
]