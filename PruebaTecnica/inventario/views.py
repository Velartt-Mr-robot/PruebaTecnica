from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm


#Definir las vistas

def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')
    
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos})

def crear(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
          
    return render(request, 'productos/crear.html', {'formulario': formulario} )

def editar(request, id):
    producto = Producto.objects.get(id=id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/editar.html', {"formulario": formulario})    

def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productos')     
    