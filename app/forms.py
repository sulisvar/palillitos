from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Contacto, Producto

class CustomUserCreationForm(UserCreationForm):

    class Meta:
     model = User
     fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

class ContactoForm(forms.ModelForm):
    
     class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]

class ProductoForm(forms.ModelForm):

     class Meta:
        model = Producto
        fields = ["nombre", "precio", "descripcion", "marca", "imagen"]
    