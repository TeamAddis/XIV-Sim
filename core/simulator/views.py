from django.views.generic.edit import FormView
from django.shortcuts import render

from core.action.forms import ActionFormSet
from core.actionloop.models import ActionLoop
from core.action.models import Action
from core.job.views import JobListByGroup

from .models import Simulator

class SimulatorView(FormView):
    template_name = 'simulator/index.html'
    form_class = ActionFormSet
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tankJobs'] = JobListByGroup().get_queryset_by_job_group('tank')
        context['healerJobs'] = JobListByGroup().get_queryset_by_job_group('healer')
        context['dpsJobs'] = JobListByGroup().get_queryset_by_job_group('dps')
        context['total_potency'] = 0
        return context

    def form_valid(self, form):
        formset = form
        simulator = Simulator()
        loop = ActionLoop(0)
        for form in formset:
            action = form.cleaned_data['action']
            if isinstance(action, Action):
                loop.add_action(action)
        simulator.add_action_loop(loop)
        context = self.get_context_data(form=formset)
        context['total_potency'] = simulator.calculate_total_potency()
        
        return render(self.request, self.template_name, context=context)