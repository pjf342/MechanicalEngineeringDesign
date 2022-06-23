from django import forms


SURFACE_CHOICES = [
    ('IN', 'Inner Surface'),
    ('OUT', 'Outer Surface'),
]
CAPPED_CHOICES = [
    ('C', 'Capped'),
    ('U', 'Uncapped'),
]


class inputPVSform(forms.Form):
    surface = forms.CharField(widget=forms.Select(choices=SURFACE_CHOICES))
    capped = forms.CharField(widget=forms.Select(choices=CAPPED_CHOICES))
    po = forms.FloatField(label='Outer Pressure', widget=forms.NumberInput(attrs={'placeholder': '(kPa)'}))
    pi = forms.FloatField(label='Inner Pressure', widget=forms.NumberInput(attrs={'placeholder': '(kPa)'}))
    do = forms.FloatField(label='Outer Diameter', widget=forms.NumberInput(attrs={'placeholder': '(mm)'}))
    di = forms.FloatField(label='Inner Diameter', widget=forms.NumberInput(attrs={'placeholder': '(mm)'}))
