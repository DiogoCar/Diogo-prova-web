# clientes/urls.py
from django.urls import path
from .views import (
    ProdutoListView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView
)
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.index, name='index'),
    path("lista/", ProdutoListView.as_view(), name="lista"),
    path("novo/", ProdutoCreateView.as_view(), name="criar"),
    path("editar/<int:pk>/", ProdutoUpdateView.as_view(), name="editar"),
    path("excluir/<int:pk>/", ProdutoDeleteView.as_view(), name="excluir"),
]