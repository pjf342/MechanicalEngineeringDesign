from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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


class inputPSform(forms.Form):
    sigma_x = forms.FloatField(label='Sigma X', widget=forms.NumberInput(attrs={'placeholder': ''}))
    sigma_y = forms.FloatField(label='Sigma Y', widget=forms.NumberInput(attrs={'placeholder': ''}))
    tau_xy = forms.FloatField(label='Tau XY', widget=forms.NumberInput(attrs={'placeholder': ''}))

    # def clean(self):
    #     if self.cleaned_data('sigma_x') == self.cleaned_data('sigma_y'):
    #         raise forms.ValidationError('Sigma X and Sigma Y can not be the same value.')


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
