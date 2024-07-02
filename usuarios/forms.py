from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        #aca van las clases
        widgets= {


        }
        error_messages = {
            'username': {
                'required': 'El nombre de usuario es obligatorio.',
                'unique': 'Este nombre de usuario ya está en uso.',
                'invalid': 'El nombre de usuario contiene caracteres inválidos.',
            },
            'email': {
                'required': 'El correo electrónico es obligatorio.',
                'invalid': 'Introduce una dirección de correo válida.',
            },
            'password1': {
                'required': 'La contraseña es obligatoria.',
                'password_mismatch': 'Las contraseñas no coinciden.',
                'password_too_similar': 'La contraseña es demasiado similar al correo electrónico.',
                'password_too_short': 'La contraseña es demasiado corta. Debe contener al menos 8 caracteres.',
                'password_too_common': 'La contraseña es demasiado común.',
                'password_entirely_numeric': 'La contraseña no puede ser completamente numérica.',
            },
            'password2': {
                'required': 'La confirmación de la contraseña es obligatoria.',
                'password_mismatch': 'Las contraseñas no coinciden.',
            },
        }

    def __init__(self, *args, **kwargs):
        super(RegistroUsuarioForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))  
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))


    
#esto ya esta full listo - no mover ni cambiar nada