import locale

from django.db import models


# Create your models here.

class TipoCuenta(models.Model):
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = 'tipo_cuenta'

    def __str__(self):
        return self.nombre


class Cuenta(models.Model):
    id = models.IntegerField(primary_key=True,
                             editable=False,
                             )
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None, null=True)
    tipo = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE, default=None, null=True)
    balance = models.FloatField(default=0)
    iban = models.TextField(default=None, null=True)

    class Meta:
        db_table = 'CUENTA'

    def __str__(self):
        return self.customer.username + " - " + self.tipo.nombre

    def get_display_balance(self):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        return locale.currency(self.balance, grouping=True)


class Movimiento(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(
        'cuentas.Cuenta', models.DO_NOTHING, db_column='account_id')
    operation_type = models.CharField(max_length=20)
    amount = models.IntegerField()
    changed_at = models.DateTimeField()

    class Meta:
        db_table = 'movimientos'
