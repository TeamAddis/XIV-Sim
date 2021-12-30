from django import forms
from django.forms import formset_factory
from django.forms.formsets import formset_factory

from .models import Action

class ActionForm(forms.Form):
    action = forms.ModelChoiceField(queryset=Action.objects.all())

ActionFormSet = formset_factory(ActionForm, extra=5)