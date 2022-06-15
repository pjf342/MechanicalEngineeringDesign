from django.shortcuts import render
from .models import PressureVesselStressApp
from .forms import PressureVesselStressForm


def pressure_vessel_create_view(request):
    form = PressureVesselStressForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "templates/pvs.html", context)


def pressure_vessel_detail_view(request):
    obj = PressureVesselStressApp.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "templates/pvs.html", context)
