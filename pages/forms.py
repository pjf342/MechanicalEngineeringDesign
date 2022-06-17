from django import forms
from django.forms import ModelForm
from .models import PVSmodel


class PVSform(ModelForm):
    class Meta:
        model = PVSmodel
        fields = ('Surface', 'Capped?', 'Inner Pressure', 'Outer Pressure', 'Inner Diameter', 'Outer Diameter')
        labels = {
            'Surface':'',
            'Capped?':'',
            'Inner Pressure':'',
            'Outer Pressure':'',
            'Inner Diameter':'',
            'Outer Diameter':'',
        }
        widgets = {
            'Inner Pressure': forms.NumberInput(attrs={'placeholder':'Inner Pressure'}),
            'Outer Pressure': forms.NumberInput(attrs={'placeholder':'Outer Pressure'}),
            'Inner Diameter': forms.NumberInput(attrs={'placeholder':'Inner Diameter'}),
            'Outer Diameter': forms.NumberInput(attrs={'placeholder':'Outer Diameter'}),
        }