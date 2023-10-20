from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from AppNico import views


urlpatterns = [
    path('', views.inicio , name= "Inicio"),
    path('leermas/', views.leer_mas , name="LeerMas"),
    path('paginas/', views.paginas , name= "Paginas"),
    path("acercademi/", views.acerca_de_mi , name="AcercaDeMi"),
    path("iniciarsesion/", views.login_request , name="IniciarSesion"),
    path("registrar", views.registro, name="Registrar"),
    path('edit/', views.editarPerfil , name = "Editar"),   
    path('logout/', LogoutView.as_view(template_name='AppNico/logout.html'), name='CerrarSesion'),
    path('blogNuevo/', BlogCreacion.as_view(), name='BlogNuevo'),
    path('blogslist/', BlogListView.as_view(), name='BlogList'),
    path('blogsdetalles/<int:pk>/', BlogDetalles.as_view(), name='BlogsDetalles'),
    path('borrar/<int:pk>/', BlogBorrar.as_view(), name='Borrar'),
    path('edit/<int:pk>/', BlogEditar.as_view(), name='Edit'),
    path('detalle/', views.detalles, name='Detalles'),
    path('blogsdetalles/<int:pk>/comentario/', ComentarioPagina.as_view(), name='Comentario'),
    
    
    
    
    
]
