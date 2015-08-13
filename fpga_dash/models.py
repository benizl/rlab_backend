from django.db import models

class Configuration(models.Model):
	de2Serial = models.CharField(max_length=100)
	ardSerial = models.CharField(max_length=100)
