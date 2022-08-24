from django.contrib import admin

from .models import Cuenta, Movimiento, TipoCuenta

# Register your models here.
admin.site.register(Cuenta)
admin.site.register(Movimiento)
admin.site.register(TipoCuenta)
