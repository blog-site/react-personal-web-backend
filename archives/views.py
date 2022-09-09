from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets
from .models import Archive
from .serializers import ArchiveSerializer
import json

class ArchiveViewSet(viewsets.ModelViewSet):
  serializer_class = ArchiveSerializer
  queryset = Archive.objects.all()
  lookup_field = 'slug'

@ensure_csrf_cookie
def HelloWorld(request):
  data = ["Hello", "World"]
  data_json = json.dumps(data)
  return HttpResponse(data_json, content_type='application/json')
