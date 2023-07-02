from django.urls import path
from .views import viewMap

urlpatterns = [
    path('', viewMap, name='home'),
    # path('add_user/', adicionar_usuario, name='add_user'),
    
]