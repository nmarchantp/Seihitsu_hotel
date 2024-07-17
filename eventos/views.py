# eventos/views.py
from django.shortcuts import render

def eventos(request):
    context={}
    return render(request, 'eventos/eventos.html', {'eventos': eventos})