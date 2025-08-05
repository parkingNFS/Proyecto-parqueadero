from rest_framework.routers import DefaultRouter
from ..rol.views import *
from ..facturas.views import *

router = DefaultRouter()

router.register(r'facturas', facturasViewset, basename='facturas')
router.register(r'hora_parking', hora_parkingViewset, basename='hora_parking')
router.register(r'rol', rolViewset, basename='rol')
router.register(r'servicio', servicioViewset, basename='servicio')
router.register(r'servicio', servicioViewset, basename='usuario')
router.register(r'vehiculo', vehiculoViewset, basename='vehiculo')

urlpatterns = router.urls