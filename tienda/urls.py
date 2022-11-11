from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('ListaProducto/', views.ListaProducto, name='ListaProducto'),
    path('tienda/', views.welcome, name='welcome'),
]
