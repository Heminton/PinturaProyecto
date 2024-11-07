from django.db import models
"""
CATALOGOS
"""

class Catalogo(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=100)
    class Meta:
        verbose_name_plural = 'Catalogos'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
