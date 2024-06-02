# web/views.py
from django.shortcuts import render

def promociones(request):
    return render(request, 'promociones.html')