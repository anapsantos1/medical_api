from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PacienteViewSet, ConsultaViewSet

router = DefaultRouter()
# router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'consultas', ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
