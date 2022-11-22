from django.urls import path
from . import views

urlpatterns = [

    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),

    path('GestionProducto/', views.GestionProducto, name='GestionProducto'),
    path('CompraProducto/', views.CompraProducto, name='CompraProducto'),
    path('Informes/', views.informes, name='Informes'),

    path('producto/nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('producto/<str:pk>', views.producto_eliminar, name='producto_eliminar'),
    path('producto/editar/<str:pk>', views.producto_editar, name='producto_editar'),

    path('producto/sabermas/<str:pk>', views.saber_mas, name='saber_mas'),
    path('producto/comprar/<str:pk>', views.producto_comprar, name='producto_comprar'),
    path('producto/comprar/checkout/<str:pk>', views.checkout, name='checkout'),

    path('Informes/Marcas/', views.marcas, name='marcas'),
    path('Informes/Marcas/Productos/<str:nombremarca>', views.productos_in_marcas, name='productos_in_marcas'),
]
