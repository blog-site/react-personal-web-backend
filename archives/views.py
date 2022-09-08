from django.shortcuts import render
from rest_framework import viewsets
from .models import Archive
from .serializers import ArchiveSerializer

class ArchiveViewSet(viewsets.ModelViewSet):
  serializer_class = ArchiveSerializer
  queryset = Archive.objects.all()
  lookup_field = 'slug'
