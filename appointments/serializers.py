from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Paciente, Consulta


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

    def create(self, validated_data):
        cpf = validated_data.get('cpf')
        paciente_existente = Paciente.objects.filter(cpf=cpf).first()

        if paciente_existente:
            raise ValidationError({
                "detail": f"Paciente com CPF {cpf} já cadastrado.",
                "paciente_id": paciente_existente.id
            })

        return super().create(validated_data)

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
