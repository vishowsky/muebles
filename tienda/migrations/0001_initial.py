# Generated by Django 4.1.3 on 2022-11-22 17:16

from django.db import migrations, models
import django.db.models.deletion
import tienda.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('nombreCategoria', models.CharField(max_length=150)),
                ('imagenCategoria', models.ImageField(blank=True, null=True, upload_to=tienda.models.rutaArchivo)),
                ('estado', models.BooleanField(default=False, help_text='0=habilitado, 1=desabilitado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('nombreProducto', models.CharField(max_length=150)),
                ('imagenProducto', models.ImageField(blank=True, null=True, upload_to=tienda.models.rutaArchivo)),
                ('descripcionProducto', models.TextField(max_length=500)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('estado', models.BooleanField(default=False, help_text='0=Disponible, 1=Sin stock')),
                ('etiqueta', models.CharField(max_length=150)),
                ('Trending', models.BooleanField(default=False, help_text='0=sin tendencia, 1=en tendencia')),
                ('diaDeCreacion', models.DateField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria')),
            ],
        ),
    ]
