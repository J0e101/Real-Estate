from django.contrib import admin
from django.urls import path
from RealEstateApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about, name='about'),
    path('properties/', views.properties, name='properties'),
    path('agents/', views.agents, name='agents'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('property-single/', views.propingles, name='property-single'),
    path('service-details/', views.servetails, name='service-details'),
]
