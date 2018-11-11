from django.db import models
from datetime import date
from mandadero_app.models import Mandadero
from client_app.models import Cliente

class Mandado(models.Model):
	done_for = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
	done_by = models.ForeignKey(Mandadero, null=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, blank=True)
	detail = models.CharField(max_length=200)

class Promociones(models.Model):
	applicable = models.ForeignKey(Mandado, on_delete=models.CASCADE)
	description = models.CharField(max_length=200)
	start_date = models.DateTimeField(auto_now_add=False)
	end_date = models.DateTimeField(auto_now_add=False)

class Lugar(models.Model):
	mandado_inplace = models.ForeignKey(Mandado, null=True, on_delete=models.SET_NULL)
	visited_by = models.ForeignKey(Mandadero, null=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	address = models.CharField(max_length=200)








