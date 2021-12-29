from django import forms
from .models import Job

class JobForm(forms.Form):
    job = forms.ModelChoiceField(queryset=Job.objects.all())