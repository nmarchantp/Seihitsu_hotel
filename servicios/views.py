# servicios/views.py
from django.shortcuts import render

def servicio(request):
    return render(request, 'servicios/servicio.html')