from django.urls import path
from AppPubg.views import *

urlpatterns = [
    path("", inicioView,name='Inicio'),
    path("player/", playerView,name='Jugadores'),
    path("maps/", mapsView,name='Mapas'),
    path("vehicles/", vehiclesView,name='Vehiculos'),
    path("equipament/", equipamentView,name='Equipamento'),
    path("weapons/", weaponsView,name='Armas'),
    path("throwable/", throwableView,name='Arrojables'),
    path("playerForm/", playerFormView,name='JugadorFormulario'),
    path("mapForm/", mapFormView,name='MapFormulario'),
    path("vehicleForm/", vehicleFormView,name='VehiculoFormulario'),
    path("equipamentForm/", equipamentFormView,name='EquipamentoFormulario'),

    path("weaponResult/", weaponSearch,name='WeaponResult'),
    ]