from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='homebase'),
    path('paginas/servicos.html', views.servicos, name='servicos'),
]