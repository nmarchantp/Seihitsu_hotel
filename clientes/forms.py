from django import forms
from .models import Cliente
from .models import TarjetaCredito

class RegistroPerfilForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id_tipo_cliente','nombre', 'segundo_nombre','apellido', 'segundo_apellido', 'numero_identificacion','nombre_empresa', 'rut',  'email', 'telefono', 'direccion',
            'comuna', 'region', 'pais'
        ]
        widgets = {            
            'id_tipo_cliente': forms.Select(attrs={'class': 'form-control', 'id': 'tipo_cliente'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu segundo nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu apellido'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu segundo apellido'}),
            'numero_identificacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu número de documento de identidad'}),
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el nombre de tu empresa'}),
            'rut': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escribe el rut de tu empresa'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu teléfono'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu dirección'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'})
           
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id_tipo_cliente','nombre', 'segundo_nombre','apellido', 'segundo_apellido', 'numero_identificacion','nombre_empresa', 'rut',  'email', 'telefono', 'direccion',
            'comuna', 'region', 'pais'
        ]
        widgets = {
            'id_tipo_cliente': forms.Select(attrs={'class': 'form-control', 'id': 'tipo_cliente', 'disabled': 'disabled'}),
            'id_user': forms.HiddenInput(),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_identificacion': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su teléfono'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'})
            
        }


class TarjetaCreditoForm(forms.ModelForm):
    class Meta:
        model = TarjetaCredito
        fields = ['numero_tarjeta', 'nombre_titular', 'fecha_expiracion']

    def save(self, commit=True):
        tarjeta_credito = super().save(commit=False)
        tarjeta_credito.set_cvv(self.cleaned_data['cvv'])  
        if commit:            
            tarjeta_credito.save()
        return tarjeta_credito