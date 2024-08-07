# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Tu cuenta ha sido creada y has sido autenticado automáticamente.')
            return redirect('index')  # Redirige a la página principal
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro_usuario.html', {'form': form})


def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("Usuario autenticado...")
                login(request, user)
                # Redirige a donde desees después del login
                return redirect('perfil')  # Cambia 'index' por tu página deseada
            else:
                return render(request,'alumnos/login.html')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login_usuario.html', {'form': form})

def logout_sesion(request):
    try:
        logout(request)
        return redirect('index')
    except:
        print("Error, no se pudo cerrar sesion...")
        return redirect('index')
    

