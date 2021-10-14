from django.urls import path
from . views import MoonPhaseView


app_name = 'moonphase'

urlpatterns = [
    path('', MoonPhaseView.as_view(), name='moon_phase'),
    ]
