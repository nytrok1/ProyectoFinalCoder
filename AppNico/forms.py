from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from AppNico.models import Blog , Comentario 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ['username', 'email' , 'password1' , 'password2']
        #saca los mensajes de ayuda 
        help_texts = {k:"" for k in fields}
    
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email','password1' , 'password2' , 'first_name' , 'last_name']
        #saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class NuevoBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('usuario', 'titulo' , 'descripcion', 'imagen' , 'ano')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'ano': forms.TextInput(attrs={'class': 'form-control'}),


            
        }

class ActualizarBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('titulo', 'descripcion')

        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('mensaje',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
            }
        

