from django.db import models

from core.job.models import Job

class Action(models.Model):
    name = models.CharField(max_length=200, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)
    action_type = models.CharField(max_length=200, choices=[
        ("weaponskill","Weaponskill"),
        ("ability","Ability"),
    ], null=True)
    cast_time = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    recast_time = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    potency = models.IntegerField(null=True, blank=True)
    combo_potency = models.IntegerField(null=True, blank=True)
    combo_action = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    ## combo_bonus = ?

    def __str__(self):
        return self.name