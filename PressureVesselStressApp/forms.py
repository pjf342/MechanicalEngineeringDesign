from django import forms
from .models import PressureVesselStressApp

class PressureVesselStressForm(forms.ModelForm):
    class Meta:
        model = PressureVesselStressApp
        fields = [
            'surface',
            'cap',
            'pouter',
            'pinner',
            'douter',
            'dinner',
        ]