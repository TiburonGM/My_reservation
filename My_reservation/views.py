from django.shortcuts import render

# Vista para listar todas las reservas
def index(request):
   return render(request, 'index.html')