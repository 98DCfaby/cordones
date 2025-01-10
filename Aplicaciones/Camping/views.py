from django.shortcuts import render,redirect,get_object_or_404
def inicio(request):
    return render(request, 'inicio.html')
from .models import Campista,Reserva

def nuevoCampista(request):
    return render(request, 'nuevoCampista.html')
def listadoCampista(request):
    campistas = Campista.objects.all()
    return render(request, 'listadoCampista.html', {'campistas': campistas})
def guardar_campista(request):
    if request.method == "POST":
        # Capturar los datos enviados por el formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        # Validar que los datos obligatorios estén presentes
        if not (nombre and apellido and correo and telefono):
            return HttpResponse("Todos los campos obligatorios deben estar llenos.", status=400)

        # Crear el objeto Campista y guardarlo en la base de datos
        nuevo_campista = Campista(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            telefono=telefono,
            direccion=direccion
        )
        nuevo_campista.save()

        # Redirigir a una página de éxito o al listado
        return redirect('/listadoCampista')
def eliminar_campista(request, id):
    campista = get_object_or_404(Campista, id=id)
    campista.delete()
    return redirect('/listadoCampista/')

def editarCampista(request, id):
    campistaEditar = get_object_or_404(Campista, id=id)
    return render(request, 'editar_campista.html', {'campista': campistaEditar})

# Actualiza los datos del campista
def actualizarCampista(request, id):
    campista = get_object_or_404(Campista, id=id)
    if request.method == 'POST':
        # Procesar los datos enviados desde el formulario
        campista.nombre = request.POST['txt_nombre']
        campista.apellido = request.POST['txt_apellido']
        campista.correo = request.POST['txt_correo']
        campista.telefono = request.POST['txt_telefono']
        campista.direccion = request.POST['txt_direccion']
        campista.save()  # Guardamos los cambios

        return redirect('/listadoCampista')  # Redirigimos a la lista de campistas

    return render(request, 'editar_campista.html', {'campista': campista})

#-------------------------------------------------------------------------------------------------------------------------------------------------------
def nuevaReserva(request):
    campistas = Campista.objects.all()  # Obtener todos los campistas para asociar con la reserva
    return render(request, 'nuevaReserva.html', {'campistas': campistas})

# Vista para listar todas las reservas
def listadoReservaCamping(request):
    reservas = Reserva.objects.all()  # Obtener todas las reservas
    return render(request, 'listadoReservaCamping.html', {'reservas': reservas})

# Vista para guardar la nueva reserva
def guardar_reserva(request):
    if request.method == "POST":
        # Captura de los datos del formulario
        campista_id = request.POST.get('campista_id')  # Asegúrate de que este campo esté presente en el formulario
        tipoalojamiento = request.POST.get('tipoalojamiento')
        numeropersonas = request.POST.get('numeropersonas')
        fechainicio = request.POST.get('fechainicio')
        fechafin = request.POST.get('fechafin')
        estadoreserva = request.POST.get('estadoreserva')
        observaciones = request.POST.get('observaciones')

        # Verifica si el campista_id es válido
        if not campista_id:
            return HttpResponse("El campista es obligatorio.", status=400)

        try:
            campista = Campista.objects.get(id=campista_id)
        except Campista.DoesNotExist:
            return HttpResponse("Campista no encontrado.", status=404)

        # Crear la reserva y guardarla
        reserva = Reserva(
            campista=campista,
            tipoalojamiento=tipoalojamiento,
            numeropersonas=numeropersonas,
            fechainicio=fechainicio,
            fechafin=fechafin,
            estadoreserva=estadoreserva,
            observaciones=observaciones
        )
        reserva.save()

        # Redirigir a una página de éxito o al listado de reservas
        return redirect('/listadoReservaCamping')
    else:
        return HttpResponse("Método no permitido.", status=405)
def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('/listadoReservaCamping/')

# Editar una reserva existente
def editar_reserva(request, id):
    reserva_editar = get_object_or_404(Reserva, id=id)
    campistas = Campista.objects.all()  # Lista de campistas para el formulario
    return render(request, 'editar_Reserva.html', {'reserva': reserva_editar, 'campistas': campistas})

# Actualiza los datos de una reserva
def actualizar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        # Procesar los datos enviados desde el formulario
        reserva.fechainicio = request.POST['fechainicio']
        reserva.fechafin = request.POST['fechafin']
        reserva.campista_id = request.POST['campista_id']
        reserva.tipoalojamiento = request.POST['tipoalojamiento']
        reserva.numeropersonas = request.POST['numeropersonas']
        reserva.estadoreserva = request.POST['estadoreserva']
        reserva.observaciones = request.POST['observaciones']
        reserva.save()  # Guardamos los cambios

        return redirect('/listadoCampista/')  # Redirigimos a la lista de reservas

    return render(request, 'editar_Reserva.html', {'reserva': reserva})