from django.shortcuts import render
from django.http import HttpResponse
from .forms import PVSform


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def pvs_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = PVSform(request.POST)
        if form.is_valid():
            form.save()
    form = PVSform
    return render(request, 'pvs.html', {'form': form})