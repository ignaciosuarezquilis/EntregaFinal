# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    # Field name made lowercase.
    customer_dni = models.TextField(db_column='customer_DNI')
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        db_table = 'CLIENTE'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        db_table = 'cuenta'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    # Field name made lowercase.
    employee_dni = models.TextField(db_column='employee_DNI')
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class MarcaTarjeta(models.Model):
    marca_tarjeta_id = models.AutoField(primary_key=True)
    # This field type is a guess.
    marca_tarjeta_nombre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamos'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class TipoCliente(models.Model):
    tipo_cliente_id = models.AutoField(primary_key=True)
    # This field type is a guess.
    tipo_cliente_nombre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_cliente'


class TipoCuenta(models.Model):
    tipo_cuenta_id = models.AutoField(primary_key=True)
    # This field type is a guess.
    tipo_cuenta_nombre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'


class TipoTarjeta(models.Model):
    tipo_tarjeta_id = models.AutoField(primary_key=True)
    # This field type is a guess.
    tipo_tarjeta_nombre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_tarjeta'
