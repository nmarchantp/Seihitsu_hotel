from django.shortcuts import render

# Create your views here.
#crea un metodo para llamar a una plantilla
def habitaciones(request):
    context={}
    return render(request, 'hoteles/habitaciones.html', {'hoteles': habitaciones}) #retorna el html correspondiente

def habitaciones_santiago(request):
    context={}
    return render(request, 'hoteles/habitaciones_santiago.html', {'hoteles': habitaciones_santiago})

def habitaciones_vina(request):
    context={}
    return render(request, 'hoteles/habitaciones_vina.html', {'hoteles': habitaciones_vina})


# def "nombre de la plantilla"(request):
#     context={}
#     return render(request, 'hoteles/habitaciones.html', {'hoteles': nombre metodo})