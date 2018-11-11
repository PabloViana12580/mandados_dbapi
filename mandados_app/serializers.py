from rest_framework import serializers
from . import models
from client_app import models as modelsClient
from mandadero_app import models as modelsMandadero

class mandado_serializer(serializers.ModelSerializer):
	done_by = modelsMandadero.Mandadero
	done_for = modelsClient.Cliente
	class Meta:
		model = models.Mandado
		fields = '__all__'

class promociones_serializer(serializers.ModelSerializer):
	applicable = models.Mandado
	class Meta:
		model = models.Promociones
		fields = '__all__'

class lugar_serializer(serializers.ModelSerializer):
	mandado_inplace = models.Mandado
	visited_by = modelsMandadero.Mandadero
	class Meta:
		model = models.Lugar
		fields = '__all__'


