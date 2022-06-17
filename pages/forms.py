from django import forms


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

    surface = forms.CharField()
    capped = forms.CharField()
    pouter = forms.FloatField(label='Outer Pressure')
    pinner = forms.FloatField(label='Inner Pressure')
    douter = forms.FloatField(label='Outer Diameter')
    dinner = forms.FloatField(label='Inner Diameter')