from django.db import models

class Venta(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    vendedor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.vendedor} - {self.monto} ({self.fecha})"
