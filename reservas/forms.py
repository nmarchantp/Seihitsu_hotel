from django import forms
from hoteles.models import Hotel
from .models import ReservaHabitacion

class RegistroFormReserva(forms.ModelForm):
    class Meta:
        model = ReservaHabitacion
        fields = [
            'id_reserva_habitacion','fecha_inicio', 'fecha_fin', 'id_habitacion'
        ]
        labels = {
            'fecha_inicio' : 'Check-in',
            'fecha_fin' : 'Check-out',

        }
        widgets = {
            'id_reserva_habitacion': forms.Select(attrs={'class': 'form-control', 'id': 'reserva_habitacion'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form_control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form_control', 'type': 'date'})
        }
        
class BuscarReservaForm(forms.Form):
    nombre_hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(), required=True)
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)

    

