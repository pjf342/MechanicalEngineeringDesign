from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import pvsForm


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def pvs_view(request, *args, **kwargs):
    return render(request, 'pvs.html', {})


def princ_str_view(request, *args, **kwargs):
    return render(request, 'principal.html', {})


def cw_view(request, *args, **kwargs):
    return render(request, 'cw.html', {})


def get_surface(request):
    if request.method == 'POST':
        form = pvsForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = pvsForm()
    return render(request, 'pvs.html', {'form': form})