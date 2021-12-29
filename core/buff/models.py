from django.db import models

class Buff(models.Model):
    name = models.CharField(max_length=200, null=True)
    duration = models.IntegerField(null=True)
    ## modifier = ?

    def __str__(self):
        return self.name

class Debuff(Buff):
    potency = models.IntegerField(null=True, blank=True)