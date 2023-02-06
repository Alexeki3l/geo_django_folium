from django.urls import path

from .views import viewMap

urlpatterns = [
    path('', viewMap, name='home'),
    
]