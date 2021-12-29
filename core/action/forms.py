from django import forms
from .models import Action

class ActionForm(forms.Form):
    action = forms.ModelChoiceField(queryset=Action.objects.all())