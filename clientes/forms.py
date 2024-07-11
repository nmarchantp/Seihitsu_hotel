from django import forms
from .models import Cliente
from .models import TarjetaCredito

class RegistroPerfilForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id_tipo_cliente', 'numero_identificacion', 'nombre', 'segundo_nombre',
            'apellido', 'segundo_apellido', 'email', 'telefono', 'direccion',
            'comuna', 'region', 'pais', 'nombre_empresa', 'rut'
        ]
        widgets = {            
            'id_tipo_cliente': forms.Select(attrs={'class': 'form-control', 'id': 'tipo_cliente'}),
            'numero_identificacion': forms.TextInput(attrs={'class': 'form-control'}),
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
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id_tipo_cliente', 'numero_identificacion', 'id_user', 'nombre', 'segundo_nombre',
            'apellido', 'segundo_apellido', 'email', 'telefono', 'direccion',
            'comuna', 'region', 'pais', 'nombre_empresa', 'rut'
        ]
        widgets = {
            'id_tipo_cliente': forms.Select(attrs={'class': 'form-control', 'id': 'tipo_cliente', 'disabled': 'disabled'}),
            'numero_identificacion': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'id_user': forms.HiddenInput(),  
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
            'rut': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'})
        }


class TarjetaCreditoForm(forms.ModelForm):
    class Meta:
        model = TarjetaCredito
        fields = ['numero_tarjeta', 'nombre_titular', 'fecha_expiracion', 'cvv_encrypted']

    def save(self, commit=True):
        tarjeta_credito = super().save(commit=False)
        if commit:
            tarjeta_credito.set_cvv(self.cleaned_data['cvv'])  # Cifrar el CVV antes de guardar
            tarjeta_credito.save()
        return tarjeta_credito