from django.db import models

# Create your models here.

class Libro(models.Model):
    libro_id = models.AutoField(primary_key=True)
    titulo = models.TextField()
    descripcion = models.TextField()
    imagen = models.TextField()
    pub_date = models.TextField()
    autor_id = models.ForeignKey("autores_categorias.Autores", on_delete=models.CASCADE)
    categoria_id = models.ForeignKey("autores_categorias.Categorias", on_delete=models.CASCADE)

    def __str__(self):
        return "%s"%(self.titulo)