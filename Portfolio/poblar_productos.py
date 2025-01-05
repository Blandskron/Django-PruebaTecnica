import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')  # Cambia 'Portfolio' por el nombre de tu proyecto
django.setup()

from database.models import Producto
from django.contrib.auth.models import User

def poblar_productos():
    # Obtener un usuario existente
    user = User.objects.first()
    if not user:
        print("No hay usuarios registrados. Por favor, crea al menos un usuario antes de ejecutar este script.")
        return

    # Datos de prueba
    productos = [
        {"nombre": "Producto 1", "descripcion": "Descripción del Producto 1", "precio": 10.0},
        {"nombre": "Producto 2", "descripcion": "Descripción del Producto 2", "precio": 20.0},
        {"nombre": "Producto 3", "descripcion": "Descripción del Producto 3", "precio": 30.0},
    ]

    # Poblar la base de datos
    for producto in productos:
        Producto.objects.create(creado_por=user, **producto)

    print("Productos de prueba creados exitosamente.")

if __name__ == '__main__':
    poblar_productos()
