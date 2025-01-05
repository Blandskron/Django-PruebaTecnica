from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    enviado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contacto de {self.nombre} ({self.email})"
