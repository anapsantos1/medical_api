from django.db import models
from professionals.models import Profissional

# Create your models here.

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.crm}"

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True) # ou 11 com mask
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Profissional, on_delete=models.CASCADE)  # atualizado
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"{self.data_hora} - {self.paciente.nome} com {self.medico.name}"
