from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_jogo, name='iniciar_jogo'),
    path('jogo/', views.jogo, name='jogo'),
    path('reiniciar/', views.reiniciar, name='reiniciar'),
]
