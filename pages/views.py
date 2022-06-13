from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'home.html', {})


def pvs_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'pvs.html', {})


def princ_str_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'principal.html', {})


def cw_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'cw.html', {})