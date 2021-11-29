from django.contrib import admin
from .models import Insumos, Registros
# Register your models here.

class InsumosAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'precio', 'descripcion', 'stock']
    search_fields= ['nombre']
    list_per_page= 5


class RegistrosAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido', 'email' , 'username', 'contraseña', 'contraseña2']
    search_fields= ['username']
    list_per_page= 7


admin.site.register(Insumos, InsumosAdmin)
admin.site.register(Registros, RegistrosAdmin)