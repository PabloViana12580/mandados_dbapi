from django.db import models

# Create your models here.
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
