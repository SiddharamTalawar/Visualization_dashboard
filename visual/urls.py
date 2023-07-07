from django.urls import path

from .views import dataView,barplotView,countryView


urlpatterns = [
    path('add_data/', dataView, ),
    path('', barplotView, name = 'homeview'),
    path('country/<str:country>/', countryView, name = 'countrysView'),
]
