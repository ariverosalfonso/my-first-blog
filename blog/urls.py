from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #Nombre de la URL que se usa para identificar la vista
    
]