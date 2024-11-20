
from django.db import models
"""
Tipos
"""

class Tipo(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=50, unique=True)
    class Meta:
        verbose_name_plural = 'Tipos'
        permissions = [
            ("puede_aprobar", "Puede aprobar registros"),
            ("puede_rechazar", "Puede rechazar registros"),
        ]

    def __str__(self):
        return f"{self.nombre}"
        # return f"{self.codigo} - {self.descripcion}"
