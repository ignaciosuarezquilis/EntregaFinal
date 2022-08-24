from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import CreateUserForm


# Create your views here.


def login_page(request):
    cxt = {}
    if request.user.is_authenticated:
        return redirect('homebanking')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homebanking')
            else:
                return redirect('login')

        return render(request, "login/login.html", cxt)


def logoutUser(request):
    logout(request)
    return redirect('login')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('homebanking')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.customer_save()

            return redirect('login')

        context = {'form': form, }
        return render(request, "login/register.html", context)
