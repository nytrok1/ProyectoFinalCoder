from django.urls import path
from AppNico import views

urlpatterns = [
    path('', views.inicio , name= "Inicio"),
    path("empleados/", views.empleados , name="Empleados"),
    path("clientes/", views.clientes , name="Clientes"),
    path("buscarproductos/", views.buscarproductos, name="BuscarProductos"),
    path('buscar/', views.buscar , name = "Buscar"),   
    
    
]
