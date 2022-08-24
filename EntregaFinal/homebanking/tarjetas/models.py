from django.db import models

# Create your models here.


class Tarjeta(models.Model):
    tarjeta_id = models.AutoField(primary_key=True)
    numero_tarjeta = models.CharField(max_length=20)
    tarjeta_cvv = models.CharField(max_length=3)
    tarjeta_fecha_de_otorgamiento = models.DateField()
    tarjeta_fecha_de_expiracion = models.DateField()
    customer_id = models.ForeignKey(
        'clientes.Cliente', models.DO_NOTHING, db_column='customer_id')

    class Meta:
        db_table = 'tarjeta'
