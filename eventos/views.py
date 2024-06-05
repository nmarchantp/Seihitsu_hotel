# eventos/views.py
from django.shortcuts import render

def eventos(request):
    return render(request, 'eventos.html')