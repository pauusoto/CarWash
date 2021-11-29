from django.urls import path
from .views import index, vision, mapa, galeria, registro, insumos, modificar_insumos, listar_insumos, modificar, eliminar_insumos

urlpatterns = [
    path('', index, name= "index"),
    path('vision/', vision, name= "vision"),
    path('mapa/', mapa, name="mapa"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('insumos/', insumos, name="insumos"),
    path('modificar_insumos/', modificar_insumos, name="modificar_insumos"),
    path('listar_insumos/', listar_insumos, name="listar_insumos"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('eliminar_insumos/<id>/', eliminar_insumos, name="eliminar_insumos"),
]