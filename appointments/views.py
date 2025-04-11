from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Especialidade, Paciente, Consulta
from rest_framework import status
from rest_framework.response import Response 
from .serializers import (
    PacienteSerializer,
    ConsultaSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend

# class EspecialidadeViewSet(viewsets.ModelViewSet):
#     queryset = Especialidade.objects.all()
#     serializer_class = EspecialidadeSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['medico']

    @action(detail=False, methods=['get'], url_path='por-profissional/(?P<profissional_id>[^/.]+)')
    def por_profissional(self, request, profissional_id=None):
        consultas = Consulta.objects.filter(medico_id=profissional_id)
        serializer = self.get_serializer(consultas, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='por-paciente/(?P<paciente_id>[^/.]+)')
    def por_paciente(self, request, paciente_id=None):
        consultas = Consulta.objects.filter(paciente_id=paciente_id)
        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='por-paciente-cpf/(?P<cpf>[^/.]+)')
    def por_paciente_cpf(self, request, cpf=None):
        try:
            paciente = Paciente.objects.get(cpf=cpf)
        except Paciente.DoesNotExist:
            return Response({"detail": "Paciente não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        consultas = Consulta.objects.filter(paciente=paciente)
        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data)
