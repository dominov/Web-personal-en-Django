from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    return render(request,"core/inicio.html")

def quienessomos(request):
   return render(request,"core/quienessomos.html")

def catalogo(request):
     return render(request,"core/catalogo.html")

def contactenos(request):
    return render(request,"core/contactenos.html")
