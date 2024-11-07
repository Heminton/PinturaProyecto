# Generated by Django 4.2.16 on 2024-10-14 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('telefono', models.CharField(max_length=15, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
