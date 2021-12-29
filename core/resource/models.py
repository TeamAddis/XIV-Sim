from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=200, null=True)
    max_value = models.IntegerField(null=True)