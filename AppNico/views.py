from django.shortcuts import render , redirect
from AppNico.forms import *
from AppNico.models import Cliente , Empleado ,Producto
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "AppNico/inicio.html")

def buscarproductos(request):
    return render(request, 'AppNico/BuscarProductos.html')   

def buscar(request):

    if request.GET['camada']:

        camada = request.GET['camada']

        cursos = Producto.objects.filter(nombre__icontains=camada)

        return render(request, "AppNico/resultados.html", {"cursos": cursos , "camada": camada })

    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)




def clientes(request):
    mi_formulario = ClienteFormulario()
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST)#aqui me llega toda la infromacion del html

        print(mi_formulario)

        if mi_formulario.is_valid(): #si paso la validacion de django

                informacion = mi_formulario.cleaned_data

                nombre = Cliente(nombre = informacion['nombre'], apellido = informacion['apellido'] , documento = informacion['documento'])

                nombre.save()

                return render(request,"AppNico/index.html") #vuelvo al inicio o donde quieran
        else:
            
            mi_formulario = ClienteFormulario() # formulario vacio para construir el html
        
    return render(request, "AppNico/clientes.html" , {"miformulario":mi_formulario})

def empleados(request):
    mi_formulario = EmpleadoFormulario()
    if request.method == "POST":
        mi_formulario = EmpleadoFormulario(request.POST)#aqui me llega toda la infromacion del html

        print(mi_formulario)

        if mi_formulario.is_valid(): #si paso la validacion de django

                informacion = mi_formulario.cleaned_data

                nombre = Empleado (nombre = informacion['nombre'], apellido = informacion['apellido'] , puesto = informacion['puesto'])

                nombre.save()

                return render(request,"AppNico/index.html") #vuelvo al inicio o donde quieran
        else:
            
            mi_formulario = EmpleadoFormulario() # formulario vacio para construir el html
        
    return render(request, "AppNico/empleados.html" , {"miformulario":mi_formulario})



