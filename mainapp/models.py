from django.db import models

# Create your models here.

class Messages(models.Model):
	title = models.CharField(max_length=200)
	field_2 = models.BooleanField(default=False)