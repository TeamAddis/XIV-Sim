from django.shortcuts import render
from django.forms import formset_factory
from django.forms.formsets import formset_factory

from core.action.forms import ActionForm
from core.actionloop.models import ActionLoop
from core.action.models import Action
from core.job.forms import JobForm

from .models import Simulator

def index(request):
    form_count = 5
    context = {'jobform': JobForm()}

    ActionFormSet = formset_factory(ActionForm, extra=form_count)

    if request.method == "POST":
        formset = ActionFormSet(request.POST)
        context["formset"] = formset

        if formset.is_valid():
            simulator = Simulator()
            loop = ActionLoop(0)
            for form in formset:
                action = form.cleaned_data['action']
                if isinstance(action, Action):
                    loop.add_action(action)
            simulator.add_action_loop(loop)
            potency = simulator.calculate_total_potency()

            context['total_potency'] = potency

    elif request.method == "GET":
        context["formset"] = ActionFormSet()
    
    return render(request, 'simulator/index.html', context=context)