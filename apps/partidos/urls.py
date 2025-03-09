from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_partidos, name='lista_partidos'),
]