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

    surface = models.CharField(max_length=5, choices=SURFACE_CHOICES, default=INNERSURFACE)
    capped = models.CharField(max_length=8, choices=CAPPED_CHOICES, default=CAPPED)
    pinner = models.FloatField()
    pouter = models.FloatField()
    dinner = models.FloatField()
    douter = models.FloatField()