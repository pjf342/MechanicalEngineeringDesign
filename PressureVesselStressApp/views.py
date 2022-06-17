from django.shortcuts import render
from .forms import PressureVesselStressForm, pvsForm


def calculate_pvs(request):
    submitted = False
    form = PressureVesselStressForm
    return render(request, "templates/pvs.html", {'form': form})
