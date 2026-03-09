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
    path('prod/', views.get_produtos, name='get_produtos'),
    path('', views.index, name='index'),
    path("lista_Prod/", ProdutoListView.as_view(), name="lista"),
    path("novo_Prod/", ProdutoCreateView.as_view(), name="criar"),
    path("editar_Prod/<int:pk>/", ProdutoUpdateView.as_view(), name="editar"),
    path("excluir_Prod/<int:pk>/", ProdutoDeleteView.as_view(), name="excluir"),
]