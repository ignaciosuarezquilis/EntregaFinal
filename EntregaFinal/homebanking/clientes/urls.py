from django.urls import path

from prestamos import views as prestamos_views
from . import views

urlpatterns = [
    path('me', views.homebanking, name='homebanking'),
    path('me/loans', prestamos_views.homebanking, name='prestamos'),
]
