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
    path('cli/', views.get_clientes, name='get_clientes'),
    path('', views.index, name='index'),
    path("lista_Cli/", ClienteListView.as_view(), name="lista"),
    path("novo_Cli/", ClienteCreateView.as_view(), name="criar"),
    path("editar_Cli/<int:pk>/", ClienteUpdateView.as_view(), name="editar"),
    path("excluir_Cli/<int:pk>/", ClienteDeleteView.as_view(), name="excluir"),
]