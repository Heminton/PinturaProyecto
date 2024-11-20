from django.db import models
"""
Proveedores
"""
class Proveedor(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    apellido = models.CharField(verbose_name='Apellidos', max_length=100)
    #longitud
    #latitud
    class Meta:
        verbose_name_plural = 'Proveedores'
        permissions = [
            ("puede_aprobar", "Puede aprobar registros"),
            ("puede_rechazar", "Puede rechazar registros"),
        ]

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"
        # return f"{self.codigo} - {self.nombre} "
