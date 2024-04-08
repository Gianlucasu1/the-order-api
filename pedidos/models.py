from django.db import models
from productos.models import Producto
from restaurantes.models import Restaurante

class Pedido(models.Model):
    ESTADOS = (
        ('EN', 'En espera'),
        ('PR', 'En preparación'),
        ('LI', 'Listo'),
    )
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='EN')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    es_para_llevar = models.BooleanField(default=False)
    nombre_cliente = models.CharField(max_length=100)

    def __str__(self):
        return f"Pedido {self.id} - {self.nombre_cliente}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"
