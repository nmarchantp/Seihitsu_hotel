from django.shortcuts import render

# Create your views here.

def hoteles(request):
    context={}
    return render(request, 'hoteles/habitaciones.html', {'hoteles': hoteles})