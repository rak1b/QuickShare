from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homeview),
    path('upload/', views.FileUploadView),
    path('upload_file/', views.upload_files),
    path('delete/', views.delete_files),
    path('delete/single/<str:uid>', views.delete_single),
    path('download/<str:uid>', views.download_files),
]
