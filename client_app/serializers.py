from rest_framework import serializers
from . import models

class cliente_serializer(serializers.ModelSerializer):
	class Meta:
		model = models.Cliente
		fields = '__all__'