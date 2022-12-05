from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homeview),
    path('upload/', views.upload_files),
    path('download/<str:uid>', views.download_files),
]
