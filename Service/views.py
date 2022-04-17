from rest_framework.parsers import JSONParser, MultiPartParser
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer
from rest_framework import filters
# Create your views here.
#订单历史
class ServiceViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['orderid__orderid', 'orderid__customer','orderid__serial']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
