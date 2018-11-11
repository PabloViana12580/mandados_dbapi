from rest_framework import viewsets
from rest_framework import mixins
from . import models, serializers

# Create your views here.
class cliente_view_set(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	queryset = models.Cliente.objects.all()
	serializer_class = serializers.cliente_serializer