# professionals/models.py

from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Profissional(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    # Campos de médico:
    crm = models.CharField(max_length=20, unique=True)
    specialty = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.crm}"

