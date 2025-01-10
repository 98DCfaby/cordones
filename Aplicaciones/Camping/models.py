from django.db import models
class Campista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo= models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    campista = models.ForeignKey(Campista, on_delete=models.CASCADE)
    tipoalojamiento = models.CharField(max_length=200)
    numeropersonas = models.CharField(max_length=200)
    estadoreserva = models.CharField(max_length=200)
    observaciones = models.TextField() 