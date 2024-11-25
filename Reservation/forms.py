from django import forms
from .models import Reserva

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['mesa', 'cliente', 'fecha', 'hora', 'duracion', 'comentario']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'mesa': forms.Select(attrs={'class': 'form-select'}),
            'cliente': forms.Select(attrs={'class': 'form-select'}),
        }
