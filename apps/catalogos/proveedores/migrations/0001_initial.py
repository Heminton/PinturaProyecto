# Generated by Django 4.2 on 2024-11-18 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellidos')),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
                'permissions': [('puede_aprobar', 'Puede aprobar registros'), ('puede_rechazar', 'Puede rechazar registros')],
            },
        ),
    ]
