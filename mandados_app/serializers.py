from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class mandadero_serializer(serializers.ModelSerializer):
	class Meta:
		model = models.Mandadero
		fields = '__all__'

class cliente_serializer(serializers.ModelSerializer):
	class Meta:
		model = models.Cliente
		fields = '__all__'

class mandado_serializer(serializers.ModelSerializer):
	done_by = models.Mandadero
	done_for = models.Cliente
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
	visited_by = models.Mandadero
	class Meta:
		model = models.Lugar
		fields = '__all__'

