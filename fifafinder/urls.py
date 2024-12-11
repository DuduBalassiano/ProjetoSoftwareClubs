from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('add_player/', views.add_player, name='add_player'),
    path('', views.home_view, name='home'),
]

from django.contrib import admin
from django.urls import path

