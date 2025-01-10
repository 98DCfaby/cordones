from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('nuevoCampista/', views.nuevoCampista),
    path('listadoCampista/', views.listadoCampista),
    path('guardar_campista/', views.guardar_campista),
    path('editar_campista/<int:id>/', views.editarCampista),
    path('actualizarCampista/<int:id>/', views.actualizarCampista),
    path('eliminar_campista/<int:id>/', views.eliminar_campista),
#----------------------------------------------------------------------------------------------------------------------------------------------------
    path('nuevaReserva/', views.nuevaReserva),
    path('listadoReservaCamping/', views.listadoReservaCamping),  # Asegúrate que esta ruta esté correcta
    path('guardar_reserva/', views.guardar_reserva),
    path('eliminar_reserva/<int:id>/', views.eliminar_reserva),
    path('editar_reserva/<int:id>/', views.editar_reserva),
    path('actualizar_reserva/<int:id>/', views.actualizar_reserva),
]