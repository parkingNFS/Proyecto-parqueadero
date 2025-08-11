from rest_framework.routers import DefaultRouter
from ..horadeparqueo.views import *
from ..medios_de_pago.views import *
from ..permisos.views import *
from ..rol.views import *
from ..tiempo.views import *
from ..tiempodeparqueo.views import *
from ..tipo_de_factura.views import *
from ..usuarios.views import *
from ..vehiculo.views import *


router = DefaultRouter()

router.register(r'horadeparqueo', HoradeparqueoViewset, basename='horadeparqueo')
router.register(r'medios_de_pago', Medios_de_pagoViewset, basename='medios_de_pago')
router.register(r'permisos', PermisosViewset, basename='permisos')
router.register(r'rol', RolViewset, basename='rol')
router.register(r'tiempo', TiempoViewset, basename='tiempo')
router.register(r'tiempodeparqueo', TiempodeparqueoViewset, basename='tiempodeparqueo')
router.register(r'tipo_de_factura', Tipo_de_facturaViewset, basename='tipo_de_factura')
router.register(r'usuarios', UsuariosViewset, basename='usuarios')
router.register(r'vehiculo', VehiculoViewset, basename='vehiculo')

urlpatterns = router.urls