import datetime
import locale

from django.db import models


# Create your models here.

class TipoPrestamo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipo_prestamo'


class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.ForeignKey(TipoPrestamo, on_delete=models.CASCADE, default=None, null=True)
    cliente = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None, null=True)
    date = models.DateField(default=datetime.date.today)
    total = models.FloatField(default=0)

    class Meta:
        db_table = 'prestamos'


class MontoMax(models.Model):
    monto = models.FloatField(default=0)
    tipo = models.OneToOneField('clientes.TipoCliente', default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'MontoMax'

    def __str__(self):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        if self.tipo is None:
            return locale.currency(self.monto, grouping=True)
        else:
            return locale.currency(self.monto, grouping=True) + f" - {self.tipo.nombre}"
