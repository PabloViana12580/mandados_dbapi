from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mandados_app import views as mandados_views
from client_app import views as client_views
from mandadero_app import views as mandadero_views

#Router creation
router = DefaultRouter()

#Client
router.register(
	r'mandadero',
	mandadero_views.mandadero_view_set,
)

router.register(
	r'cliente',
	client_views.cliente_view_set,
)

router.register(
	r'mandado',
	mandados_views.mandado_view_set,
)

router.register(
	r'promos',
	mandados_views.promociones_view_set,
)

router.register(
	r'lugar',
	mandados_views.lugar_view_set,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]




