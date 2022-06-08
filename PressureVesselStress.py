import numpy as np
import math
import sys


class PressureVesselStress:
    """

    """
    def __init__(self, surface, capped, pouter, pinner, douter, dinner):
        """

        :param surface: True = outer, False = inner
        :type surface: bool
        :param capped: True = capped, False - uncapped
        :type capped: bool
        :param pouter: Outer pressure (kPa)
        :type pouter: float
        :param pinner: Inner pressure (kPa)
        :type pinner: float
        :param douter: Outer diameter (mm)
        :type douter: float
        :param dinner: Inner diameter (mm)
        :type dinner: float
        """
        self.stress_t = None
        self.stress_r = None
        self.stress_a = None
        self.capped = capped
        self.po = pouter
        self.pi = pinner
        self.do = douter / 1000
        self.di = dinner / 1000
        self.surface = surface
        self.thick_walled = None
        self.t = (self.do - self.di) / 2
        self.ro = self.do / 2
        self.ri = self.di / 2

        if self.surface:
            self.r = self.do / 2
            self.p = self.po
        if not self.surface:
            self.r = self.di / 2
            self.p = self.pi

        self.tr = self.t / self.r

        if self.tr >= .1:
            self.thick_walled = True
        if self.tr < .1:
            self.thick_walled = False

        self.tangential_stress()
        self.radial_stress()
        self.axial_stress()

    def tangential_stress(self):
        if self.thick_walled:
            if self.po != 0:
                self.stress_t = (self.pi * (self.ri ** 2) - self.po * (self.ro ** 2) - (self.ri ** 2) * (self.ro **2) * (self.po - self.pi) / (self.r ** 2)) / ((self.ro ** 2) - (self.ri ** 2))
            if self.po == 0:
                self.stress_t = ((self.ri ** 2) * self.pi) / ((self.ro ** 2) - (self.ri ** 2)) * (1 + ((self.ro ** 2) / (self.r ** 2)))
        if not self.thick_walled:
            self.stress_t = (self.p * (self.di + self.t)) / (2 * self.t)

    def radial_stress(self):
        if self.thick_walled:
            if self.po != 0:
                self.stress_r = (self.pi * (self.ri ** 2) - self.po * (self.ro ** 2) + (self.ri ** 2) * (self.ro ** 2) * (self.po - self.pi) / (self.r ** 2)) / ((self.ro ** 2) - (self.ri ** 2))
            if self.po == 0:
                self.stress_t = ((self.ri ** 2) * self.pi) / ((self.ro ** 2) - (self.ri ** 2)) * (1 - ((self.ro ** 2) / (self.r ** 2)))
        if not self.thick_walled:
            self.stress_t = 0

    def axial_stress(self):
        if self.capped:
            if self.thick_walled:
                if self.po != 0:
                    self.stress_a = (self.pi * (self.ri ** 2) - self.po * (self.ro ** 2)) / ((self.ro ** 2) - (self.ri ** 2))
                if self.po == 0:
                    self.stress_a = (self.pi * (self.ri ** 2)) / ((self.ro ** 2) - (self.ri ** 2))
            if not self.thick_walled:
                self.stress_a = (self.p * self.di) / (4 * self.t)
        if not self.capped:
            self.stress_a = 0


if __name__ == "__main__":
    pi = math.pi
