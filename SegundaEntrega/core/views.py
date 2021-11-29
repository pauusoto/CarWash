from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Insumos
from .forms import InsumosForm
from .forms import RegistrosForm
from .models import Registros
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.

def index(request):
    return render (request, 'core/index.html')

def vision(request):
    return render (request, 'core/vision.html')

def mapa(request):
    return render (request, 'core/mapa.html')

def galeria(request):
    return render (request, 'core/galeria.html' )


def registro(request):
    datos= {
        'form' : RegistrosForm()
    }
    if request.method== 'POST' :
        formulario = RegistrosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] ="Usuario creado correctamente"
    return render (request, 'core/registro.html', datos )

@login_required 
def insumos(request):
    datos= {
        'form' : InsumosForm()
    }
    if request.method== 'POST' :
        formulario = InsumosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] ="Insumo Guardado Correctamente"


    return render (request, 'core/insumos.html', datos )

@login_required
def modificar_insumos(request):
    insumosAll= Insumos.objects.all()
    datosa= {
        'listaInsumos' : insumosAll
    }
    return render (request, 'core/modificar_insumos.html', datosa )

@login_required
def listar_insumos(request):
    insumosAll= Insumos.objects.all()
    datos= {
        'listaInsumos' : insumosAll
    }
    return render (request, 'core/listar_insumos.html', datos )

@login_required
def modificar(request, id):
    insumos = Insumos.objects.get(id=id)
    datos= {
        'form' : InsumosForm(instance=insumos)
    }
    if request.method == 'POST':
        formulario = InsumosForm(data=request.POST, instance=insumos)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Empleado modificado correctamente"
            datos['form'] = formulario
    return render(request, 'core/modificar.html', datos)

@login_required
def eliminar_insumos(request, id):
    insumos = Insumos.objects.get(id=id)
    insumos.delete()

    return redirect(to="modificar_insumos")
    