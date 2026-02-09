# clientes/urls.py
from django.urls import path
from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView
)
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.index, name='index'),
    path("lista/", ClienteListView.as_view(), name="lista"),
    path("novo/", ClienteCreateView.as_view(), name="criar"),
    path("editar/<int:pk>/", ClienteUpdateView.as_view(), name="editar"),
    path("excluir/<int:pk>/", ClienteDeleteView.as_view(), name="excluir"),
]