from django.db import models

# Create your models here.


class PressureVesselStressApp(models.Model):

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

    surface = models.CharField(max_length=100, choices=SURFACES)
    capped = models.CharField(max_length=100, choices=CAP)
    pouter = models.FloatField(max_length=100)
    pinner = models.FloatField(max_length=100)
    douter = models.FloatField(max_length=100)
    dinner = models.FloatField(max_length=100)