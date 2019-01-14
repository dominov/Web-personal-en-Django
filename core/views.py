from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi Web personal</h1>
<ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/quienessomos/">Quienes Somos</a></li>
    <li><a href="/catalogo/">Catalogo</a></li>
    <li><a href="/contactenos/">Contactenos</a></li>
</ul>    
"""

# Create your views here.
def inicio(request):
    return HttpResponse(html_base+ """
    <h2>Portada</h2>
    <p>Esto es la portada</p>
"""    
    )

def quienessomos(request):
    return HttpResponse(html_base+ """
    <h2>Quienes Somos</h2>
    <p>Esta es una web para mi uso personal</p>
"""    
    )

def catalogo(request):
    return HttpResponse(html_base+ """
    <h2>Catalogo</h2>
    <p>Estos son los productos que ofrezco</p>
"""    
    )

def contactenos(request):
    return HttpResponse(html_base+ """
    <h2>Contactenos</h2>
    <p>Esto es la portada</p>
"""    
    )
