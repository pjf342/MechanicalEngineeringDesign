from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def pvs_view(request, *args, **kwargs):
    return render(request, 'pvs.html', {})