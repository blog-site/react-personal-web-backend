from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets, status
from rest_framework.response import Response
from datetime import datetime
import json
from .models import Archive
from .serializers import ArchiveSerializer

class ArchiveViewSet(viewsets.ModelViewSet):
  serializer_class = ArchiveSerializer
  queryset = Archive.objects.all()
  lookup_field = 'slug'
  # permission_classes = [permissions.AllowAny]

  def create(self, request, *args, **kwargs):
    now = datetime.utcnow().isoformat(sep='T') + 'Z'
    request.data['date_created'] = now
    request.data['date_modified'] = now
    request.data['date_published'] = now

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

  def partial_update(self, request, *args, **kwargs):
    now = datetime.utcnow().isoformat(sep='T') + 'Z'
    request.data['date_modified'] = now
    if (request.data['published']):
      request.data['date_published'] = now

    kwargs['partial'] = True
    return self.update(request, *args, **kwargs)

@ensure_csrf_cookie
def HelloWorld(request):
  data = ["Hello", "World"]
  data_json = json.dumps(data)
  return HttpResponse(data_json, content_type='application/json')
