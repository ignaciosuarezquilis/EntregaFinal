import datetime
import locale

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cuentas.models import Cuenta, TipoCuenta
from .models import TipoPrestamo, Prestamo, MontoMax


# Create your views here.
@login_required()
def homebanking(request):
    context = {}
    if request.method == "POST":
        return post_solicitud(request)

    tipos = TipoPrestamo.objects.all()
    context['tipos'] = tipos
    return render(request, "prestamos/prestamos.html", context)


def post_solicitud(request):
    errors = False
    tipo = request.POST.get('tipo')

    if tipo is None:
        messages.error(request, 'Debe seleccionar un tipo de prestamo')
        return redirect('prestamos')
    else:
        tipo = int(tipo)

    fecha = datetime.datetime.strptime(request.POST.get('fecha'), '%Y-%m-%d')
    monto = float(request.POST.get('monto'))

    if monto <= 0:
        messages.error(request, 'El monto debe ser mayor a 0')
        return redirect('prestamos')

    user = request.user

    try:
        tipo_cuenta = TipoCuenta.objects.get(nombre="Cuenta Ahorro")
        cuenta = Cuenta.objects.get(customer=user, tipo_id=tipo_cuenta)

        try:
            monto_max = MontoMax.objects.get(tipo_id=tipo)
        except MontoMax.DoesNotExist:
            monto_max = MontoMax(monto=0)

        if monto > monto_max.monto:
            messages.error(request, f'El monto no puede ser mayor a: {str(monto_max)}')
            errors = True
        else:
            cuenta.balance = cuenta.balance + monto

    except TipoCuenta.DoesNotExist:
        messages.error(request, 'No existe el tipo Cuenta de Ahorro')
        errors = True
    except Cuenta.DoesNotExist:
        messages.error(request, 'No existe una CA para el Usuario')
        errors = True
    except Cuenta.MultipleObjectsReturned:
        messages.error(request, 'Existe mas de una cuenta de ahorro para el usuario')
        errors = True

    if errors is False:
        cuenta.save()
        prestamo = Prestamo(tipo_id=tipo, date=fecha, total=monto, cliente=user)
        prestamo.save()
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        messages.success(request, f'Prestamo de {locale.currency(prestamo.total, grouping=True)} solicitado')
        return redirect('homebanking')
    else:
        return redirect('prestamos')
