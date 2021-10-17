import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .moon_phase_calculator import get_lunar_phase


class MoonPhaseView(LoginRequiredMixin, View):
    def get(self, request):
        dt = datetime.date.today()
        moon_phase, moon_age = get_lunar_phase(dt)
        messages.success(request, f'Hello {request.user} !')
        messages.success(request, 'Welcome to our Space Station!')
        context = {
            'current_date': dt,
            'moon_phase': moon_phase,
            'moon_age': moon_age
        }
        return render(request, 'moonphase/moonphase.html', context)
