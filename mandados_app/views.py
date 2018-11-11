from rest_framework import viewsets
from rest_framework import mixins
from . import models, serializers

# Create your views here.
class mandado_view_set(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	queryset = models.Mandado.objects.all()
	serializer_class = serializers.mandado_serializer

class promociones_view_set(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	queryset = models.Promociones.objects.all()
	serializer_class = serializers.promociones_serializer

class lugar_view_set(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	queryset = models.Lugar.objects.all()
	serializer_class = serializers.lugar_serializer