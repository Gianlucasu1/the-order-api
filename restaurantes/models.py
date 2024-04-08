# Create your models here.


from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.CharField(max_length=255)
    informacion_contacto = models.TextField()

    def __str__(self):
        return self.nombre
