from django.db import models

from apps.catalogos.departamentos.models import Departamento

"""
Municipio
"""

class Municipio(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    departamento = models.ForeignKey(Departamento,verbose_name='Departamento', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Municipios'
        permissions = [
            ("puede_aprobar", "Puede aprobar registros"),
            ("puede_rechazar", "Puede rechazar registros"),
        ]

    def __str__(self):
        return f"{self.nombre}"
        # return f"{self.codigo} - {self.nombre}"