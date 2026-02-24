# fornecedores/urls.py
from django.urls import path
from .views import (
    FornecedorListView,
    FornecedorCreateView,
    FornecedorUpdateView,
    FornecedorDeleteView
)
from . import views

app_name = 'fornecedores'

urlpatterns = [
    path('forn/', views.get_fornecedores, name='get_fornecedores'),
    path('', views.index, name='index'),
    path("lista/", FornecedorListView.as_view(), name="lista"),
    path("novo/", FornecedorCreateView.as_view(), name="criar"),
    path("editar/<int:pk>/", FornecedorUpdateView.as_view(), name="editar"),
    path("excluir/<int:pk>/", FornecedorDeleteView.as_view(), name="excluir"),
]
