from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .forms import FornecedorForm 
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views import View
from rest_framework.decorators import api_view
from .serializers import FornecedorSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Fornecedor

@api_view(['GET'])
def get_fornecedores(request):

    if request.method == 'GET': 
       fornecedores = Fornecedor.objects.all()
       serializer = FornecedorSerializer(fornecedores, many=True)
       return Response(serializer.data)

    return Response(status.HTTP_404_NOT_FOUND)


def index(request):
    return render(request, "fornecedores/index.html")

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = "fornecedores/lista.html"
    context_object_name = "fornecedores"



class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "fornecedores/form.html"
    success_url = reverse_lazy("fornecedores:lista")



class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "fornecedores/form.html"
    success_url = reverse_lazy("fornecedores:lista")



class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = "fornecedores/excluir.html"
    success_url = reverse_lazy("fornecedores:lista")

