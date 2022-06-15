from django import forms
from .models import PressureVesselStressApp


class PressureVesselStressForm(forms.ModelForm):
    class Meta:
        model = PressureVesselStressApp
        fields = [
            'surface',
            'capped',
            'pouter',
            'pinner',
            'douter',
            'dinner',
        ]