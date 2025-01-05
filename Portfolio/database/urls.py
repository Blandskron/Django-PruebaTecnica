from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto_list, name='producto_list'),
    path('create/', views.producto_create, name='producto_create'),
    path('update/<int:pk>/', views.producto_update, name='producto_update'),
    path('delete/<int:pk>/', views.producto_delete, name='producto_delete'),
]
