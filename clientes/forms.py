from django import forms
from .models import Cliente


class ClienteFormRegistro(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id_tipo_cliente', 'numero_identificacion', 'id_user', 'nombre', 'segundo_nombre',
            'apellido', 'segundo_apellido', 'email', 'telefono', 'direccion',
            'comuna', 'region', 'pais', 'nombre_empresa', 'rut'
        ]
        widgets = {
            'numero_identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_tipo_cliente': forms.Select(attrs={'class': 'form-control', 'id': 'tipo_cliente'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su teléfono'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'})
            # Añade más widgets según necesites
        }
