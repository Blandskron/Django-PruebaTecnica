from django.shortcuts import render
from .models import Venta
import matplotlib.pyplot as plt
import io
import urllib, base64
from datetime import datetime

def reporte_ventas_mensuales(request):
    # Consultar datos de ventas
    ventas = Venta.objects.all()

    # Filtrar por el mes actual
    mes_actual = datetime.now().month
    ventas_mes = ventas.filter(fecha__month=mes_actual)

    # Agrupar por vendedor y sumar las ventas
    ventas_por_vendedor = {}
    for venta in ventas_mes:
        ventas_por_vendedor[venta.vendedor] = ventas_por_vendedor.get(venta.vendedor, 0) + float(venta.monto)

    # Generar gráfico
    vendedores = list(ventas_por_vendedor.keys())
    montos = list(ventas_por_vendedor.values())

    plt.bar(vendedores, montos, color='skyblue')
    plt.title(f"Ventas del Mes ({datetime.now().strftime('%B')})")
    plt.xlabel("Vendedores")
    plt.ylabel("Monto de Ventas")
    plt.tight_layout()

    # Convertir gráfico a imagen
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'queries/reporte.html', {'graphic': graphic})
