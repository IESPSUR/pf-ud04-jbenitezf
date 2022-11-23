from django.urls import path
from . import views

urlpatterns = [

    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),

    path('tienda/admin/', views.GestionProducto, name='GestionProducto'),
    path('CompraProducto/', views.CompraProducto, name='CompraProducto'),
    path('Informes/', views.informes, name='Informes'),

    path('nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('eliminar/<str:pk>', views.producto_eliminar, name='producto_eliminar'),
    path('edicion/<str:pk>', views.producto_editar, name='producto_editar'),

    path('producto/sabermas/<str:pk>', views.saber_mas, name='saber_mas'),
    path('producto/comprar/<str:pk>', views.producto_comprar, name='producto_comprar'),
    path('producto/comprar/checkout/<str:pk>', views.checkout, name='checkout'),

    path('Informes/Marcas/', views.marcas, name='marcas'),
    path('Informes/Marcas/Productos/<str:nombremarca>', views.productos_in_marcas, name='productos_in_marcas'),
    path('Informes/Top/Productos/', views.top_ten, name='top_ten'),
]
