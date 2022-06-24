from django.shortcuts import render
from django.http import HttpResponseRedirect
import PressureVesselStress, StrengthAndColdWork, PrincipalStresses
from .forms import inputPVSform, inputSCWform, inputPSform


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


def scw_view(request, *args, **kwargs):
    user = request.user
    true_strain = None
    new_yield = None
    new_ultimate = None
    if request.method == 'POST':
        SCW_input = inputSCWform(request.POST)
        if SCW_input.is_valid():
            material_number = int(request.POST.get('material_number'))
            cold_work_percent = int(request.POST.get('cold_work_percent'))

            SCW = StrengthAndColdWork.StrengthAndColdWork(material_number, cold_work_percent)
            true_strain = float(SCW.true_strain)
            new_yield = float(SCW.new_yield)
            new_ultimate = float(SCW.new_ultimate)
    else:
        SCW_input = inputSCWform()
    SCW_data = {'SCW_input': SCW_input, 'true_strain': true_strain, 'new_yield': new_yield, 'new_ultimate': new_ultimate}
    return render(request, 'scw.html', SCW_data)


def ps_view(request, *args, **kwargs):
    user = request.user
    s_avg = None
    s1 = None
    s2 = None
    phi1 = None
    phi2 = None
    t_max = None
    shear_phi1 = None
    shear_phi2 = None
    if request.method == 'POST':
        PS_input = inputPSform(request.POST)
        if PS_input.is_valid():
            sigma_x = float(request.POST.get('sigma_x'))
            sigma_y = float(request.POST.get('sigma_y'))
            tau_xy = float(request.POST.get('tau_xy'))

            PS = PrincipalStresses.PrincipalStresses(sigma_x, sigma_y, tau_xy)
            s_avg = float(PS.s_avg)
            s1 = float(PS.s1)
            s2 = float(PS.s2)
            phi1 = float(PS.phi1)
            phi2 = float(PS.phi2)
            t_max = float(PS.t_max)
            shear_phi1 = float(PS.shear_phi1)
            shear_phi2 = float(PS.shear_phi2)
    else:
        PS_input = inputPSform()
    PS_data = {'PS_input': PS_input, 's_avg': s_avg,  's1': s1, 's2': s2, 'phi1': phi1, 'phi2': phi2, 't_max': t_max,
               'shear_phi1': shear_phi1, 'shear_phi2': shear_phi2,}
    return render(request, 'ps.html', PS_data)
