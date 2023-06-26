from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext

from ordenamiento.models import *

from ordenamiento.forms import *

def index(request):
    
    return render(request, 'index.html')


def listadoParroquias(request):
    
    parroquias = Parroquia.objects.all()
    
    titulo = "Listado de parroquias y sus barrios"
    informacion_template = {'parroquias': parroquias, 'mititulo': titulo}
    return render(request, 'listadoParroquias.html', informacion_template)

def crearParroquia(request):
    
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(listadoParroquias)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario)

def editarParroquia(request, id):
    
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listadoParroquias)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario)

def listadoBarrios(request):
    
    barrios = Barrio.objects.all()
    
    titulo = "Listado de Barrios"
    informacion_template = {'barrios': barrios,
    'mititulo': titulo}
    return render(request, 'listadoBarrios.html', informacion_template)

def crearBarrio(request, id):
    
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listadoParroquias)
    else:
        formulario = BarrioForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'crearBarrio.html', diccionario)

def editarBarrio(request, id):
    
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioEditForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listadoParroquias)
    else:
        formulario = BarrioEditForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)

def eliminarBarrio(request, id):
    
    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(listadoParroquias)