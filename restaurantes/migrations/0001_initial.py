# Generated by Django 5.0.4 on 2024-04-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=255)),
                ('informacion_contacto', models.TextField()),
            ],
        ),
    ]
