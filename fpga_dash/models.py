from django.db import models

class DashSession(models.Model):
	expire = models.DateTimeField()
