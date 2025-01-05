import os
import django
from datetime import datetime, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')  # Cambia 'Portfolio' al nombre de tu proyecto
django.setup()

from queries.models import Venta

def poblar_ventas():
    vendedores = ["Alice", "Bob", "Charlie", "Diana"]
    for _ in range(50):
        vendedor = random.choice(vendedores)
        fecha = datetime.now() - timedelta(days=random.randint(0, 30))
        monto = round(random.uniform(100, 1000), 2)
        Venta.objects.create(vendedor=vendedor, fecha=fecha, monto=monto)
    print("Datos de ventas creados.")

if __name__ == '__main__':
    poblar_ventas()
