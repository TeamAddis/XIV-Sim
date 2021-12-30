from django.views.generic.list import ListView

from .models import Job

class JobListByGroup(ListView):
    model = Job
    
    def get_queryset_by_job_group(self, group_name):
        return super().get_queryset().filter(job_group=group_name)

    