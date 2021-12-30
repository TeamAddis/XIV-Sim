from django.urls import path

from .views import JobListByGroup

urlpatterns = [
    path('', JobListByGroup.as_view(), name='job-list'),
]
