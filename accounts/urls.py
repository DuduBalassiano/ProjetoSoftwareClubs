from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('add_player/', views.add_player, name='add_player'),
    path('add_championship/', views.add_championship, name='add_championship'),
    path('', views.home, name='home'),
]