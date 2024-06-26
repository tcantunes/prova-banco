from django.db import models
from django.urls import reverse


class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

    def get_absolute_url(self):
        return reverse('carro_detail', args=[str(self.id)])

