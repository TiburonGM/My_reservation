"""
URL configuration for My_reservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Reservation import views as re
from . import views as index
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index.index, name = 'index'),
    path('list', re.reservacion_view, name = 'reservation_list'),
    path('list2', re.reser, name = 'reservation_list2'),
    path('crear/', re.create_reservation, name='reservation_create'),
    path('crear2/', re.create, name='create'),
    path('crearuser/', re.crate_user, name='crate_user'),
    path('login/', auth_views.LoginView.as_view(), name='login')
]
