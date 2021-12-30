from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=200, null=True)
    job_group = models.CharField(max_length=200, choices=[
        ("tank","Tank"),
        ("healer","Healer"),
        ("dps","DPS"),
    ], null=True)
    ## resources = ?

    def __str__(self):
        return self.name
