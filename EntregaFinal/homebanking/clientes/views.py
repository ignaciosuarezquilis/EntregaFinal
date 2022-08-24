from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required()
def homebanking(request):
    context = {}
    user = request.user
    ca = user.cuenta_set.filter(tipo__nombre="Cuenta Ahorro").get()
    context['cuenta'] = ca
    return render(request, "clientes/home.html", context)
