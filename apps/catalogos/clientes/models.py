from django.db import models
"""
Clientes
"""

class Cliente(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    apellido = models.CharField(verbose_name='Apellidos', max_length=100)
    telefono = models.CharField(verbose_name='Telefono', max_length=15)
    direccion = models.CharField(verbose_name='Dirección', max_length=100)
    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.apellido} - {self.telefono} - {self.direccion}"
