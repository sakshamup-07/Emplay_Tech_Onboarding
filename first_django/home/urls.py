from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    
    path('' , views.delta , name = 'delta'),
    path('services/' , views.services , name = 'services'),
    ]
