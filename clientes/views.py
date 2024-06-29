# clientes/views.py
from django.shortcuts import render, redirect
from .forms import ClienteForm

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Cambia 'success_page' por la URL de tu página de éxito
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/cliente_form.html', {'form': form})