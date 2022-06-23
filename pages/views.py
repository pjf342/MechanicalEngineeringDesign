from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PVSform


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def pvs_view(request, *args, **kwargs):
    user = request.user
    if request.method == 'POST':
        PVS_input = PVSform(request.POST)
        if PVS_input.is_valid():
            surface = request.POST.get('surface')
            capped = request.POST.get('capped')
            po = request.POST.get('po')
            pi = request.POST.get('pi')
            do = request.POST.get('do')
            di = request.POST.get('di')
            print(po)
    else:
        PVS_input = PVSform()

    return render(request, 'pvs.html', {'PVS_input': PVS_input})

