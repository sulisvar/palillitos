from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, ContactoForm, ProductoForm
from django.contrib import messages
from .models import  Producto
from django.contrib.auth.decorators import login_required, permission_required

from rest_framework import status
from rest_framework import viewsets

from .serializer import ProductoSerializer

# consumo api
from urllib.request import urlopen
import json

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class=ProductoSerializer
    queryset = Producto.objects.all()

def home(request):

    url="https://api.gael.cl/general/public/monedas/UF"
    datos = urlopen(url).read()
    moneda = json.loads(datos)
    valor =moneda["Valor"]

    return render(request, "app/home.html",{"valorUF":valor})


def contacto(request):
   data = {
       'form': ContactoForm()
   }

   if request.method == 'POST':
      formulario = ContactoForm(data=request.POST)
      if formulario.is_valid():
         formulario.save()
         data["mensaje"] = "contacto guardado"
      else:
         data["form"] = formulario

   return render(request, 'app/contacto.html', data)


def faqs(request):
   return render(request, 'app/faqs.html')


def registro(request):
   data = {
       'form': CustomUserCreationForm()
   }

   if request.method == 'POST':
      formulario = CustomUserCreationForm(data=request.POST)
      if formulario.is_valid():
         formulario.save()
         user = authenticate(
             username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
         login(request, user)
         messages.success(request, "Te has registrado correctamente")
         return redirect(to="home")
      data["form"] = formulario

   return render(request, 'registration/registro.html', data)

@permission_required('app.add_producto')
def agregar_producto(request):

   data = {
       'form': ProductoForm()
   }

   if request.method == 'POST':
      formulario = ProductoForm(data=request.POST, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         data["mensaje"] = "guardado correctamente"
      else:
         data["form"] = formulario

   return render(request, 'app/producto/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(request):
   productos = Producto.objects.all()

   data = {
      'productos': productos
   }

   return render(request, 'app/producto/listar.html' ,data)

@permission_required('app.changue_producto')
def modificar_producto(request, id):   

   producto = get_object_or_404(Producto, id=id)

   data = {
      'form': ProductoForm(instance=producto)
   }

   if request.method == 'POST':
      formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         return redirect(to="listar_productos")
      data["form"] = formulario

   return render(request, 'app/producto/modificar.html', data)

@permission_required('app.delete_producto')  
def eliminar_producto(request, id):
   producto = get_object_or_404(Producto, id=id)
   producto.delete()
   return redirect(to="listar_productos")

