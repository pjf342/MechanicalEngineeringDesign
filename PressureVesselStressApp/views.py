from django.shortcuts import render
from .forms import PressureVesselStressForm
# Create your views here.

def pressure_vessel_create_view(request):
    form = PressureVesselStressForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'form': form
        }
        return render(request, "")

def pressure_vessel_detail_view(request):
    obj = Pres
    return render(request, "Pressure")