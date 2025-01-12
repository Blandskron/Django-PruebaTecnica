from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto_view, name='contacto'),
    path('gracias/', views.gracias_view, name='gracias'),
]
