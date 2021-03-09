from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/', views.home, name='home'),
    path('home', views.home, name='home'),
    path('uploaddata', views.upload_data, name='upload_data'),
    path('viewdata', views.view_data, name='view_data'),
]