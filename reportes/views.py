# reportes/views.py
from django.shortcuts import render

def reporte1(request):
    return render(request, 'reporte1.html')