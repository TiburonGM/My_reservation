from django.shortcuts import render, redirect
from .models import Reserva, Mesa, Cliente  # Modelo de reserva Y TABLAS
from .forms import ReservationForm, ClienteForm # Formulario para crear reservas
from django.contrib import messages #para mostrar un mensaje de exito o error
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Vista para listar todas las reservas
def reservacion_view(request):
   reservaciones = Reserva.objects.all().order_by("fecha","hora")  # Obtiene todas las reservas
   return render(request, 'reservation_list.html', {'reservaciones': reservaciones})

def reser(request):
    reservaciones = Reserva.objects.all().order_by("fecha","hora")   
    return render(request, 're_list.html', {'reservaciones': reservaciones})

# Vista para crear una nueva reserva
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Verificar disponibilidad
            date = form.cleaned_data['fecha']
            time = form.cleaned_data['hora']
            table = form.cleaned_data['mesa']

            existing_reservation = Reserva.objects.filter(fecha=date, hora=time, mesa=table).exists()
            if existing_reservation:
                messages.error(request, "La mesa ya está reservada en ese horario.")
            else:
                form.save()  # Guarda la nueva reserva
                messages.success(request, "Reservación creada con éxito.")
                return redirect("reservation_list")  # Redirige a la lista de reservas
    else:
        form = ReservationForm()
        
        return render(request, 'create_reservation.html', {'form': form})
        
def create(request):
    form = ReservationForm()
    return render(request, 'create.html', {'form': form})

def crate_user(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Verificar disponibilidad
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            nombre = form.cleaned_data['nombre']

            existing_user = Cliente.objects.filter(email=email, telefono=telefono, nombre=nombre).exists()
            if existing_user:
                messages.error(request, "Usuario Existente.")
            else:
                form.save()  # Guarda la nueva reserva
                messages.success(request, "Usuario creado con éxito.")
                return redirect("reservation_list")  # Redirige a la lista de reservas
    else:   
        form = ClienteForm()
        return render(request, 'create_user.html', {'form': form})

def login_form(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Inicia sesión y redirige al panel de administración
            login(request, user)
            messages.success(request, '¡Has iniciado sesión con éxito!')
            return redirect('admin/')  # Cambia 'admin_dashboard' por el nombre de tu URL para el panel
        else:
            # Si la autenticación falla, muestra un mensaje de error
            messages.error(request, "Usuario o contraseña incorrectos")

    # Si es un GET o falla la autenticación, renderiza la página de login
    return render(request, 'login.html')

    @login_required
    def admin_dashboard(request):
        return render(request, 'admin/')