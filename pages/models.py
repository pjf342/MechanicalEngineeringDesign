from django.db import models
from django.contrib.auth.models import UserManager


class PVSmodel(models.Model):
    INNERSURFACE = 'IN'
    OUTERSURFACE = 'OUT'
    SURFACE_CHOICES = (
        (INNERSURFACE, 'Inner Surface'),
        (OUTERSURFACE, 'Outer Surface'),
    )
    CAPPED = 'C'
    UNCAPPED = 'U'
    CAPPED_CHOICES = (
        (CAPPED, 'Capped'),
        (UNCAPPED, 'Uncapped')
    )

    surface = models.CharField(name='Surface', max_length=5, choices=SURFACE_CHOICES, default='Inner Surface')
    capped = models.CharField(name='Capped?', max_length=8, choices=CAPPED_CHOICES, default='Capped')
    pinner = models.FloatField(name='Inner Pressure')
    pouter = models.FloatField(name='Outer Pressure')
    dinner = models.FloatField(name='Inner Diameter')
    douter = models.FloatField(name='Outer Diameter')