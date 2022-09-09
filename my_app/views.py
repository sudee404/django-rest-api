from django.shortcuts import render
from rest_framework import viewsets
from .models import Project, Service
from .serializers import ProjectSerializer, ServiceSerializer
# Create your views here.


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceSerializer
    permission_classes = []


class ProjectViewSet(viewsets.ModelViewSet):
    """This is the viewset that handles all actions at /projects endpoint"""
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer
    permission_classes = []
