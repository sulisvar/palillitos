   
from django.urls import include, path
from .views import contacto, faqs, home, registro, agregar_producto, modificar_producto, listar_productos, eliminar_producto, ProductoViewSet
from app import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('productoApi',ProductoViewSet)

urlpatterns  =  [
        path('', views.home, name="home"),
        path('contacto/', contacto, name="contacto"),
        path('faqs/', faqs, name="faqs"),
        path('registro/', registro, name="registro"),
        path('agregar-producto/', agregar_producto, name="agregar_producto"),
        path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
        path('listar-productos/', listar_productos, name="listar_productos"),
        path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
        path('api/',include(router.urls)),
         ]

