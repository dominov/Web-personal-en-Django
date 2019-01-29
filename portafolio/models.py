from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200) 
    descripcion = models.TextField()
    imagen = models.ImageField()
    created =models.DateField(auto_now=True)
    update =models.DateField(auto_now=True)
