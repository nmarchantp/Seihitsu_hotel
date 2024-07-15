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
    CHOICES = [(hotel.nombre, hotel.nombre) for hotel in Hotel.objects.all()]
    
    nombre_hotel = forms.ChoiceField(choices=CHOICES, label='Hotel')
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de inicio')
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de fin')

    def clean_fecha_fin(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_fin = self.cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin:
            if fecha_fin < fecha_inicio:
                raise forms.ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")

        return fecha_fin