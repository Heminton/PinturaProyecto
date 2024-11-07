# Generated by Django 4.2.16 on 2024-11-07 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='almacen',
            options={'permissions': [('puede_aprobar', 'Puede aprobar registros'), ('puede_rechazar', 'Puede rechazar registros')], 'verbose_name_plural': 'Almacenes'},
        ),
        migrations.AddField(
            model_name='almacen',
            name='latitud',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='almacen',
            name='longitud',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
