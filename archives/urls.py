from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

app_name = 'archive'
urlpatterns = [
  path('hello/', views.HelloWorld, name='hello_world')
]

routerArchives = DefaultRouter()
routerArchives.register(r'view', views.ArchiveViewSet, basename='view')
urlpatterns += routerArchives.urls
