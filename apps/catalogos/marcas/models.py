from django.db import models
"""
Marcas
"""

class Marca(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=50, unique=True)
    class Meta:
        verbose_name_plural = 'Marcas'
        permissions = [
            ("puede_aprobar", "Puede aprobar registros"),
            ("puede_rechazar", "Puede rechazar registros"),
        ]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
