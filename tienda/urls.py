from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('GestionProducto/', views.GestionProducto, name='GestionProducto'),
    path('CompraProducto/', views.CompraProducto, name='CompraProducto'),
    path('Informes/', views.informes, name='Informes'),
    path('tienda/', views.welcome, name='welcome'),
    path('producto/nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('producto/comprar/<str:pk>', views.producto_comprar, name='producto_comprar'),
    path('producto/<str:pk>', views.producto_eliminar, name='producto_eliminar'),
    path('producto/editar/<str:pk>', views.producto_editar, name='producto_editar'),
    path('Informes/Marcas/', views.marcas, name='marcas'),
]
