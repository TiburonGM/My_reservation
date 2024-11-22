# Generated by Django 5.1.3 on 2024-11-16 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('capacidad', models.IntegerField()),
                ('ubicacion', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('duracion', models.IntegerField(default=2)),
                ('comentario', models.TextField(blank=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservation.Cliente')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservation.Mesa')),
            ],
            options={
                'unique_together': {('mesa', 'fecha', 'hora')},
            },
        ),
    ]
