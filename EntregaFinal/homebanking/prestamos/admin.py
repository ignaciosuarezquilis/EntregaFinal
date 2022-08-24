from django.contrib import admin

from .models import Prestamo, MontoMax, TipoPrestamo

# Register your models here.

admin.site.register(Prestamo)
admin.site.register(MontoMax)
admin.site.register(TipoPrestamo)
