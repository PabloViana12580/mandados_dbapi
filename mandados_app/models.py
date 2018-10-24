from django.db import models
from datetime import date

class Mandadero(models.Model):
	id_document = models.IntegerField(default=0)
	genre = models.CharField(max_length=10)
	telephone = models.IntegerField(default=0)
	name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField(max_length=70)
	description = models.CharField(max_length=200)
	used_to = models.CharField(max_length=200)
	age = models.IntegerField(default=0)
	username = models.CharField(max_length=20, default='testman')
	password = models.CharField(max_length=20, default='uvg')

class Cliente(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	genre = models.CharField(max_length=10)
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=70)
	last_name = models.CharField(max_length=20)
	id_document = models.IntegerField(default=0)
	telephone = models.IntegerField(default=0)
	age = models.IntegerField(default=0)

class Mandado(models.Model):
	done_by = models.ForeignKey(Mandadero, null=True, on_delete=models.SET_NULL)
	done_for = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
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







