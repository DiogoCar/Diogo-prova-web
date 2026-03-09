from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .forms import ClienteForm 
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views import View
from rest_framework.decorators import api_view
from .serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente

@api_view(['GET'])
def get_clientes(request):

    if request.method == 'GET': 
       clientes = Cliente.objects.all()
       serializer = ClienteSerializer(clientes, many=True)
       return Response(serializer.data)

    return Response(status.HTTP_404_NOT_FOUND)






def index(request):
    return render(request, "clientes/index.html")

class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/lista.html"
    context_object_name = "clientes"



class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form.html"
    success_url = reverse_lazy("clientes:lista")



class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form.html"
    success_url = reverse_lazy("clientes:lista")



class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "clientes/excluir.html"
    success_url = reverse_lazy("clientes:lista")

