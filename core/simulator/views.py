from django.views.generic.edit import FormView

from core.action.forms import ActionForm, ActionFormSet
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
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

def index(request):
    form_count = 5
    context = {
        "tankJobs": JobListByGroup().get_queryset_by_job_group('tank'),
        "healerJobs": JobListByGroup().get_queryset_by_job_group('healer'),
        "dpsJobs": JobListByGroup().get_queryset_by_job_group('dps'),
    }

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