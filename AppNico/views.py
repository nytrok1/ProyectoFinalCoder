from django.shortcuts import render  , redirect
from AppNico.forms import *
from AppNico.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView , UpdateView , DeleteView 
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login , authenticate 
from .forms import UserRegisterForm , UserEditForm
from django.http import Http404 





# Create your views here.

def inicio(request):
    blogs = Blog.objects.all()
    return render(request, 'AppNico/inicio.html', {'blogs': blogs})

def detalles(request):
    blogs = Blog.objects.all()
    return render(request, 'AppNico/detalles.html', {'blogs': blogs})

def leer_mas(request):
    return render(request, 'AppNico/leer_mas.html')

def paginas(request):
    
    return render(request, "AppNico/paginas.html")

def acerca_de_mi(request):
    return render(request, "AppNico/acerca_de_mi.html")

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")

            clave = form.cleaned_data.get("password")

            nombre_usuario = authenticate(username = usuario, password = clave)

            if usuario is not None:
                login (request, nombre_usuario)
                return render(request, "AppNico/iniciaste_sesion.html", {"name": usuario , "mensaje":f"Has iniciado sesión en TuBlog. Bienvenido {usuario}"})

            else:
                
                return render(request, "AppNico/iniciaste_sesion.html", {"mensaje":"Error, datos incorrectos", "form": form})

        else:

            return render(request, "AppNico/iniciaste_sesion.html", {"mensaje":"Error, formulario inválido"})

    form = AuthenticationForm()

    return render(request, "AppNico/login.html", {"form":form})

def registro(request):
        form = UserRegisterForm()
        if request.method == 'POST':

            

            form = UserRegisterForm(request.POST)

            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()

                return render(request,"AppNico/inicio.html" ,  {"mensaje":f"{username} Usuario Creado :)"})
        else:

            form = UserRegisterForm()     

        return render(request,"AppNico/registro.html" ,  {"form":form})

@login_required
def editarPerfil(request): 

    usuario = request.user
    
    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)
        

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            if informacion["password1"] != informacion['password2']:
                datos = {
                    'nombre' : usuario.nombre,
                    'email' : usuario.email
                }

                miFormulario = UserEditForm(initial=datos)
            else:

                usuario.email = informacion['email']
                usuario.set_password(informacion['password1'])
                usuario.first_name = informacion['first_name']
                usuario.last_name = informacion['last_name']

                usuario.save()

                return render(request, "AppNico/inicio.html")
        
    else:
        datos= {
            'first_name' : usuario.first_name,
            'email' : usuario.email,
            'last_name' : usuario.last_name,
        }

        miFormulario = UserEditForm(initial=datos)


    return render(request, "AppNico/edicion_usuario.html" , {"mi_form": miFormulario})

#BLOG 
class BlogCreacion(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = NuevoBlog
    success_url = reverse_lazy('Inicio')
    template_name = 'AppNico/blog_creacion.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(BlogCreacion, self).form_valid(form)
    
class BlogListView(LoginRequiredMixin , ListView):
    model = Blog 
    template_name = 'blog/blog_list.html'
    context_object_name = "blogs"
    
class BlogDetalles(LoginRequiredMixin,DetailView):
    model = Blog
    template_name = 'AppNico/blog_detalle.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context

class BlogBorrar(LoginRequiredMixin , DeleteView):
    model = Blog
    success_url = reverse_lazy('BlogList')

    def get_object(self, queryset=None):
        
        blog = super(BlogBorrar, self).get_object()

        if blog.usuario == self.request.user:
            return blog
        else:
            raise Http404("No tienes permiso para eliminar este blog.")


class BlogBorrar(LoginRequiredMixin , DeleteView):
    model = Blog
    success_url = reverse_lazy('BlogList')

    def get_object(self, queryset=None):
        
        blog = super(BlogBorrar, self).get_object()

        if blog.usuario == self.request.user:
            return blog
        else:
            raise Http404("No tienes permiso para eliminar este blog.")

class BlogEditar(LoginRequiredMixin ,UpdateView):
    model = Blog
    template_name = "AppNico/blog_editar.html"
    success_url = reverse_lazy('BlogList')
    fields = ['usuario', 'titulo', 'descripcion', 'imagen', 'ano']

    def get_object(self, queryset=None):
        
        blog = super(BlogEditar, self).get_object()

        
        if blog.usuario == self.request.user:
            return blog
        else:
            raise Http404("No tienes permiso para editar este blog.")

        

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppNico/comentarios.html'
    success_url = reverse_lazy('Inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        form.instance.nombre  = self.request.user.username
        return super(ComentarioPagina, self).form_valid(form)


