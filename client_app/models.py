from django.db import models

# Create your models here.
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