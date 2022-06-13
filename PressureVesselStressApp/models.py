from django.db import models

# Create your models here.
class PressureVesselStressApp(models.Model)
    SURFACES = ('Inner', 'Outer')
    CAPPED = ('Capped', 'Uncapped')

    surface = models.CharField(max_length=1, choices=SURFACES)
    capped = models.CharField(max_length=1, choices=CAPPED)
    pouter = models.FloatField(max_length=100)
    pinner = models.FloatField(max_length=100)
    douter = models.FloatField(max_length=100)
    dinner = models.FloatField(max_length=100)