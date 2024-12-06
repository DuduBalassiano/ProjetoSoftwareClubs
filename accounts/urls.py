from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('', views.home, name='home'),
]