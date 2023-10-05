from django import forms


class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    documento = forms.IntegerField()

class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    puesto = forms.CharField()

class BuscarProductoForm(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()
    