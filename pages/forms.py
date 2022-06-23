from django import forms
from django.forms import ModelForm


SURFACE_CHOICES = [
    ('IN', 'Inner Surface'),
    ('OUT', 'Outer Surface'),
]
CAPPED_CHOICES = [
    ('C', 'Capped'),
    ('U', 'Uncapped'),
]


class PVSform(forms.Form):
    surface = forms.CharField(widget=forms.Select(choices=SURFACE_CHOICES))
    capped = forms.CharField(widget=forms.Select(choices=CAPPED_CHOICES))
    po = forms.FloatField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Outer Pressure (kPa)'}))
    pi = forms.FloatField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Inner Pressure (kPa)'}))
    do = forms.FloatField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Outer Diameter (mm)'}))
    di = forms.FloatField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Inner Diameter (mm)'}))
