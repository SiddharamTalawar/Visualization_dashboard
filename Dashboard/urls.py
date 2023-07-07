from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from dataApi import views



router = routers.DefaultRouter()
router.register(r'data', views.DataAPIView, 'data')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('visual.urls')),
    path('registration/', include('django.contrib.auth.urls') ),
    path('registration/',include('registration.urls')),
    path('api/', include(router.urls)),
]
