from django import forms
from .models import Reserva
from .models import Cliente

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

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email']
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),   
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
        }