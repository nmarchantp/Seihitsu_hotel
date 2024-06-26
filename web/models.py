from django.db import models

#clase promocion, donde colocamos las propiedades de alguna promiocion
class Promocion(models.Model):
    id_promocion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Promoción'
        verbose_name_plural = 'Promociones'
        db_table = 'promocion'