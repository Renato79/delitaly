from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contactus/', views.contactus, name='contactus'),
    path('privacy/', views.contactus, name='privacy'),
    path('sent/', views.contactus, name='sent'),
    path('shipping/', views.contactus, name='shipping'),            
]