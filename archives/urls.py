from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

routerArchives = DefaultRouter()
routerArchives.register(r'archives', views.ArchiveViewSet, basename='archives')

app_name = 'archives'
urlpatterns = []

urlpatterns += routerArchives.urls
