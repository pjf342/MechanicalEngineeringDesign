from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse('<h1> HELLO HOME </h1>')
    return render(request, 'home.html', {})


def pvs_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse('<h1> Pressure Vessel Stresses </h1>')
    return render(request, 'pvs.html', {})


def princ_str_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse('<h1> Principal Stresses </h1>')
    return render(request, 'principal.html', {})


def cw_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse('<h1> Strength and Cold Working </h1>')
    return render(request, 'cw.html', {})