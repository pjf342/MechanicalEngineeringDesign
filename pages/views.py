from django.shortcuts import render
from django.http import HttpResponseRedirect
import PressureVesselStress
from .forms import inputPVSform


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def pvs_view(request, *args, **kwargs):
    user = request.user
    st = None
    sr = None
    sa = None
    if request.method == 'POST':
        PVS_input = inputPVSform(request.POST)
        if PVS_input.is_valid():
            if request.POST.get('surface') == 'IN':
                surface = False
            else:
                surface = True
            if request.POST.get('capped') == 'C':
                capped = True
            else:
                capped = False
            po = float(request.POST.get('po'))
            pi = float(request.POST.get('pi'))
            do = float(request.POST.get('do'))
            di = float(request.POST.get('di'))

            PVS = PressureVesselStress.PressureVesselStress(surface, capped, po, pi, do, di)
            st = float(PVS.stress_t * 1000)
            sr = float(PVS.stress_r * 1000)
            sa = float(PVS.stress_a * 1000)

    else:
        PVS_input = inputPVSform()
    PVS_data = {'PVS_input': PVS_input, 'st': st, 'sr': sr, 'sa': sa}
    return render(request, 'pvs.html', PVS_data)

