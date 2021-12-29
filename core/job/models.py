from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=200, null=True)
    ## resources = ?

    def __str__(self):
        return self.name
