from django.db import models

# Create your models here.

class Autores(models.Model):
    autor_id = models.AutoField(primary_key=True)
    nombre = models.TextField()

    def __str__(self):
        return "%s"%(self.nombre)

class Categorias(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.TextField()

    def __str__(self):
        return "%s"%(self.nombre)