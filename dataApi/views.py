from django.shortcuts import render
from rest_framework import viewsets
from visual.models import Content
from .serializers import ContentSerializer
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

class DataAPIView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    # if request is made using get method then follwing view will be called.
    def get (self, request, *args, **kwargs):
        # fetching json_data from request.
        json_data = request.body
        # Converting json_data to stream, then parsing it to python_data.
        stream = io.BytesIO(json_data)
        python_data = JSONParser.parse(stream)
        # if the request has country name then get it, else use None. 
        country = python_data.get('country', None )
        if country is not None:
            queryset = Content.objects.filter(country = country)
            serializer = ContentSerializer(queryset)
            return JsonResponse(serializer.data) 
        queryset = Content.objects.all()
        serializer = ContentSerializer(queryset, many = True)
        return JsonResponse(serializer.data) 



    
    
  

