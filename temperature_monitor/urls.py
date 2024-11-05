# temperature_monitor/urls.py

from django.contrib import admin
from django.urls import path
from dashboard.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),  # Page d'accueil du tableau de bord
]
