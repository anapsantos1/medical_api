from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfissionalViewSet, EspecialidadeViewSet

router = DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'', ProfissionalViewSet)  # Coloque por último

urlpatterns = [
    path('', include(router.urls)),
]

