from django import forms


SURFACE_CHOICES = [
    ('IN', 'Inner Surface'),
    ('OUT', 'Outer Surface'),
]
CAPPED_CHOICES = [
    ('C', 'Capped'),
    ('U', 'Uncapped'),
]
MATERIAL_CHOICES = [
    ('1018', '1018 Steel - Annealed'),
    ('1144', '1144 Steel - Annealed'),
    ('1212', '1212 Steel - Hot Rolled'),
    ('1045', '1045 Steel - Quenched and Tempered: 600\u00b0F'),
    ('4142', '4142 Steel - Quenched and Tempered: 600\u00b0F'),
    ('303', '303 Stainless Steel - Annealed'),
    ('304', '304 Stainless Steel - Annealed'),
    ('2011', '2011 Aluminum Alloy - T6'),
    ('2024', '2024 Aluminum Alloy - T4'),
    ('7075', '7075 Aluminum Alloy - T6'),
]


class inputPVSform(forms.Form):
    surface = forms.CharField(widget=forms.Select(choices=SURFACE_CHOICES))
    capped = forms.CharField(widget=forms.Select(choices=CAPPED_CHOICES))
    po = forms.FloatField(label='Outer Pressure', widget=forms.NumberInput(attrs={'placeholder': '(kPa)'}))
    pi = forms.FloatField(label='Inner Pressure', widget=forms.NumberInput(attrs={'placeholder': '(kPa)'}))
    do = forms.FloatField(label='Outer Diameter', widget=forms.NumberInput(attrs={'placeholder': '(mm)'}))
    di = forms.FloatField(label='Inner Diameter', widget=forms.NumberInput(attrs={'placeholder': '(mm)'}))


class inputSCWform(forms.Form):
    material_number = forms.CharField(widget=forms.Select(choices=MATERIAL_CHOICES))
    cold_work_percent = forms.IntegerField(label='Cold Work Percent', min_value=0, max_value=100,
                                           widget=forms.NumberInput(attrs={'placeholder': '(%)'}))
