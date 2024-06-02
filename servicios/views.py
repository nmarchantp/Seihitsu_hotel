# servicios/views.py
from django.shortcuts import render

def servicio1(request):
    return render(request, 'servicio1.html')