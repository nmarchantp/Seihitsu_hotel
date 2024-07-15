from django.shortcuts import render

# Create your views here.
#crea un metodo para llamar a una plantilla
def habitaciones(request):
    context={}
    return render(request, 'hoteles/habitaciones.html', {'hoteles': habitaciones}) #retorna el html correspondiente

# def "nombre de la plantilla"(request):
#     context={}
#     return render(request, 'hoteles/habitaciones.html', {'hoteles': nombre metodo})