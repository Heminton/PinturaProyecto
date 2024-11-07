from django.db import models
"""
Estados
"""
class Estado(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=100)
    orden = models.IntegerField(verbose_name='Orden', blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Estados'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion} - {self.orden}"


    def save(self, *args, **kwargs):
        # Lógica para establecer el campo 'orden' según 'descripcion'
        if self.descripcion == 'Procesando':
            self.orden = 1
        elif self.descripcion == 'Completado':
            self.orden = 2
        elif self.descripcion == 'Cancelado':
            self.orden = 3
        super(Estado, self).save(*args, **kwargs)