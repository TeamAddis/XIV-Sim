from django.urls import path

from .views import SimulatorView

urlpatterns = [
    path('', SimulatorView.as_view(), name='index'),
]