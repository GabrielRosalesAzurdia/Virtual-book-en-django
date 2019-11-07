from django.db import models

# Create your models here.

class ListaDeseos(models.Model):
    lista_id = models.AutoField(primary_key=True)
    libro_id = models.ForeignKey("libros.Libro", on_delete=models.CASCADE)
    usuario_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

class ListaRentados(models.Model):
    lista_id = models.AutoField(primary_key=True)
    libro_id = models.ForeignKey("libros.Libro", on_delete=models.CASCADE)
    usuario_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)