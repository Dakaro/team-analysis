from django.urls import path

from . import views

urlpatterns = [
    path('', views.playerList, name='playerList'),
]
