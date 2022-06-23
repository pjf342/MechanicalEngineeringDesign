from django.db import models

SURFACE_CHOICES = [
    ('IN', 'Inner Surface'),
    ('OUT', 'Outer Surface'),
]
CAPPED_CHOICES = [
    ('C', 'Capped'),
    ('U', 'Uncapped'),
]


class PVSmodel(models.Model):
    surface = models.CharField(max_length=15, choices=SURFACE_CHOICES)
    capped = models.CharField(max_length=15, choices=CAPPED_CHOICES)
    po = models.FloatField()
    pi = models.FloatField()
    do = models.FloatField()
    di = models.FloatField()
