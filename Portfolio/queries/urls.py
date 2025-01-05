from django.urls import path
from . import views

urlpatterns = [
    path('reporte-ventas/', views.reporte_ventas_mensuales, name='reporte_ventas'),
]
