# Generated by Django 5.0.4 on 2024-04-07 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0002_remove_producto_categoria_delete_categoriaproducto'),
        ('restaurantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('EN', 'En espera'), ('PR', 'En preparación'), ('LI', 'Listo')], default='EN', max_length=2)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('es_para_llevar', models.BooleanField(default=False)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantes.restaurante')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('observaciones', models.TextField(blank=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='pedidos.pedido')),
            ],
        ),
    ]
