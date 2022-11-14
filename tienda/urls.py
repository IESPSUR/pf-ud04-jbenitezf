from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('ListaProducto/', views.ListaProducto, name='ListaProducto'),
    path('tienda/', views.welcome, name='welcome'),
    path('producto/nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('producto/<str:pk>', views.producto_eliminar, name='producto_eliminar'),
    path('producto/editar/<str:pk>', views.producto_editar, name='producto_editar'),
]
