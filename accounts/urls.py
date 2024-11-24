from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),          # Página inicial dentro de /login/
    path('perfil/', views.perfil_view, name='perfil'), # Página de perfil
    path('cadastro/', views.cadastro_view, name='cadastro'), # Página de cadastro
]

