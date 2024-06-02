# mantenedores/views.py
from django.shortcuts import render

def mantenedor1(request):
    return render(request, 'mantenedor1.html')