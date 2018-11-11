from rest_framework import serializers
from . import models

class mandadero_serializer(serializers.ModelSerializer):
	class Meta:
		model = models.Mandadero
		fields = '__all__'
