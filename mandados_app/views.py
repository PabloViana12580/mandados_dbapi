from rest_framework import viewsets
from rest_framework import mixins
from . import models, serializers

# Create your views here.
class mandadero_view_set(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	queryset = models.Mandadero.objects.all()
	serializer_class = serializers.mandadero_serializer

class cliente_view_set(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	queryset = models.Cliente.objects.all()
	serializer_class = serializers.cliente_serializer

class mandado_view_set(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	queryset = models.Mandado.objects.all()
	serializer_class = serializers.mandadero_serializer

class promociones_view_set(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	queryset = models.Promociones.objects.all()
	serializer_class = serializers.promociones_serializer

class lugar_view_set(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	queryset = models.Lugar.objects.all()
	serializer_class = serializers.lugar_serializer