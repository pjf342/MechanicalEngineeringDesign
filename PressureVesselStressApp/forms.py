from django import forms
from .models import PressureVesselStressApp

class PressureVesselStressForm(forms.ModelForm):
    class Meta:
        model = PressureVesselStressApp
        fields = (
            'surface',
            'capped',
            'pouter',
            'pinner',
            'douter',
            'dinner',
        )


class pvsForm(forms.Form):
    INNER = 'IN'
    OUTER = 'OUT'
    SURFACES = [
        (INNER, 'Inner'),
        (OUTER, 'Outer')
    ]

    CAPPED = 'C'
    UNCAPPED = 'U'
    CAP = [
        (CAPPED, 'Capped'),
        (UNCAPPED, 'Uncapped')
    ]

    surface = models.CharField(maxlength=100, choices=SURFACES)
    capped = models.CharField(maxlength=100, choices=CAP)
    pouter = models.FloatField(label='Outer Pressure', maxlength=100)
    pinner = models.FloatField(label='Inner Pressure', maxlength=100)
    douter = models.FloatField(label='Outer Diameter', maxlength=100)
    dinner = models.FloatField(label='Inner Diameter', maxlength=100)