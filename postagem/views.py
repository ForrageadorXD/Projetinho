from django.shortcuts import render
from .models import Produto

# Create your views here.
def index(request):
    lista = Produto.objects.all()
    context={'produtos' : lista}
    return render(request,"index.html",context)

def loja(request):
    lista = Produto.objects.all()
    context={'produtos' : lista}
    return render(request,"loja.html",context)

def quemsomos(request):
    lista = Produto.objects.all()
    context={'produtos' : lista}
    return render(request,"quemsomos.html",context)

def aventura(request):
    lista = Produto.objects.all()
    context={'produtos' : lista}
    return render(request,"cat-aventura.html",context)

def fps(request):
    lista = Produto.objects.all()
    context={'produtos' : lista}
    return render(request,"cat-fps.html",context)

def detalhes(request,id):
    lista = Produto.objects.all()
    produto = Produto.objects.get(id=id)
    context={'produto' : produto}
    return render(request,"detalhes.html",context)

def categoria(request,id):
    lista = Produto.objects.all()
    produto = Produto.objects.get(id=id)
    context={'produto' : produto}
    return render(request,"categorias.html",context)