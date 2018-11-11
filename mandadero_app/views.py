from rest_framework import viewsets
from rest_framework import mixins
from . import models, serializers
# Create your views here.
class mandadero_view_set(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	queryset = models.Mandadero.objects.all()
	serializer_class = serializers.mandadero_serializer
	