from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contactus/', views.contactus, name='contactus'),
    path('privacy/', views.privacy, name='privacy'),
    path('sent/', views.sent, name='sent'),
    path('shipping/', views.shipping, name='shipping'),            
]