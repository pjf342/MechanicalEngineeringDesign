from django import forms
from django.forms import ModelForm
from .models import PVSmodel


class PVSform(ModelForm):
    class Meta:
        model = PVSmodel
        fields = ('surface', 'capped', 'pinner', 'pouter', 'dinner', 'douter')
