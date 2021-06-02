from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/sheet', views.apiSheet, name='apiSheet')
]
