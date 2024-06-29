# usuarios/views.py
from django.shortcuts import render

def usuarios(request):
    return render(request, 'usuario.html')