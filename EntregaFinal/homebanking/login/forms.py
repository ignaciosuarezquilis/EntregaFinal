from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, CharField, PasswordInput, NumberInput, DecimalField

from clientes.models import Cliente, TipoCliente
from cuentas.models import Cuenta, TipoCuenta


class CreateUserForm(UserCreationForm):
    password1 = CharField(
        label="Contraseña",
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control mb-2", }),
    )
    password2 = CharField(
        label="Confirmar contraseña",
        widget=PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control mb-3", }),
        strip=False,
        help_text="Ingrese la misma contraseña que arriba.",
    )
    dni = DecimalField(
        label="DNI",
        widget=NumberInput(attrs={"class": "form-control mb-2",
                                  "placeholder": "DNI sin puntos", }),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'dni', 'email', 'password1', 'password2', ]
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Nombre de usuario',
            }),
            'email': EmailInput(attrs={'class': 'form-control mb-2',
                                       'placeholder': 'tu@mail.com',
                                       }),
            'first_name': TextInput(attrs={'class': 'form-control mb-2',
                                           'placeholder': 'Nombre',
                                           }),
            'last_name': TextInput(attrs={'class': 'form-control mb-2',
                                          'placeholder': 'Apellido',
                                          }),
        }

    @staticmethod
    def create_cuenta(user):
        cuenta = Cuenta(customer=user)

        try:
            tipo = TipoCuenta.objects.get(nombre='Cuenta Ahorro')
            cuenta.tipo = tipo
        except TipoCuenta.DoesNotExist:
            tipo = TipoCuenta(nombre='Cuenta Ahorro')
            tipo.save()

        cuenta.save()
        return cuenta

    def create_customer(self, user):
        customer = Cliente(user=user, customer_dni=self.cleaned_data['dni'])
        try:
            tipo = TipoCliente.objects.get(nombre='Classic')
            customer.tipo = tipo
        except TipoCliente.DoesNotExist:
            tipo = TipoCliente(nombre='Classic')
            tipo.save()
        customer.save()
        return customer

    def customer_save(self, commit=True):
        user = self.save(commit=commit)
        if commit:
            self.create_customer(user)
            self.create_cuenta(user)
        return user
