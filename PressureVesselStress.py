import numpy as np
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class PVSWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pressure Vessel Stress')
        self.x = 1000  # GUI size parameters
        self.y = 1000
        self.width = 1150
        self.height = 875
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.surface = None
        self.capped = None
        self.p_outer = None
        self.p_inner = None
        self.d_inner = None
        self.d_outer = None
        self.tangential_stress = None
        self.radial_stress = None
        self.axial_stress = None

        self.info_label1 = QLabel('Cylindrical pressure vessels experience radial and tangential stresses. Examples '
                                  'are hydraulic cylinders, gun barrels, and pipes carrying fluids at high pressures.',
                                  self)
        self.info_label1.setFont(QFont('Arial', 10))
        self.info_label1.adjustSize()
        self.info_label1.move(10, 10)

        self.info_label2 = QLabel('If the pressure vessel is closed, there will be an axial stress as well.', self)
        self.info_label2.setFont(QFont('Arial', 10))
        self.info_label2.adjustSize()
        self.info_label2.move(10, 30)

        self.confirm_btn = QPushButton('Confirm', self)
        self.confirm_btn.setFont(QFont('Arial', 12))
        self.confirm_btn.setEnabled(True)
        self.confirm_btn.clicked.connect(self.confirm_button)
        self.confirm_btn.move(150, 475)
        self.confirm_btn.adjustSize()

        self.surface_label = QLabel('Inner or Outer Surface', self)
        self.surface_label.setFont(QFont('Arial', 12))
        self.surface_label.move(50, 150)
        self.surface_label.adjustSize()

        self.capped_label = QLabel('Capped or Uncapped', self)
        self.capped_label.setFont(QFont('Arial', 12))
        self.capped_label.move(50, 200)
        self.capped_label.adjustSize()

        self.p_inner_label = QLabel('Inner Pressure (Pa)', self)
        self.p_inner_label.setFont(QFont('Arial', 12))
        self.p_inner_label.move(50, 300)
        self.p_inner_label.adjustSize()

        self.p_outer_label = QLabel('Outer Pressure (Pa)', self)
        self.p_outer_label.setFont(QFont('Arial', 12))
        self.p_outer_label.move(50, 250)
        self.p_outer_label.adjustSize()

        self.d_outer_label = QLabel('Outer Diameter (mm)', self)
        self.d_outer_label.setFont(QFont('Arial', 12))
        self.d_outer_label.move(50, 350)
        self.d_outer_label.adjustSize()

        self.d_inner_label = QLabel('Inner Diameter (mm)', self)
        self.d_inner_label.setFont(QFont('Arial', 12))
        self.d_inner_label.move(50, 400)
        self.d_inner_label.adjustSize()

        self.surface_cb = QComboBox(self)
        self.surface_cb.addItems(['Inner Surface', 'Outer Surface'])
        self.surface_cb.setFont(QFont('Arial', 12))
        self.surface_cb.move(250, 150)
        self.surface_cb.adjustSize()

        self.capped_cb = QComboBox(self)
        self.capped_cb.addItems(['Capped', 'Uncapped'])
        self.capped_cb.setFont(QFont('Arial', 12))
        self.capped_cb.move(250, 200)
        self.capped_cb.adjustSize()

        self.outer_pressure = QDoubleSpinBox(self)
        self.outer_pressure.setRange(0, 999999999)
        self.outer_pressure.setFont(QFont('Arial', 12))
        self.outer_pressure.move(250, 250)
        self.outer_pressure.adjustSize()

        self.inner_pressure = QDoubleSpinBox(self)
        self.inner_pressure.setRange(0, 999999999)
        self.inner_pressure.setFont(QFont('Arial', 12))
        self.inner_pressure.move(250, 300)
        self.inner_pressure.adjustSize()

        self.outer_diameter = QDoubleSpinBox(self)
        self.outer_diameter.setRange(0, 999999999)
        self.outer_diameter.setFont(QFont('Arial', 12))
        self.outer_diameter.move(250, 350)
        self.outer_diameter.adjustSize()

        self.inner_diameter = QDoubleSpinBox(self)
        self.inner_diameter.setRange(0, 999999999)
        self.inner_diameter.setFont(QFont('Arial', 12))
        self.inner_diameter.move(250, 400)
        self.inner_diameter.adjustSize()

        self.tangential_stress_label = QLabel('Tangential Stress:', self)
        self.tangential_stress_label.setFont(QFont('Arial', 12))
        self.tangential_stress_label.move(450, 150)
        self.tangential_stress_label.adjustSize()

        self.radial_stress_label = QLabel('Radial Stress:', self)
        self.radial_stress_label.setFont(QFont('Arial', 12))
        self.radial_stress_label.move(450, 200)
        self.radial_stress_label.adjustSize()

        self.axial_stress_label = QLabel('Axial Stress:', self)
        self.axial_stress_label.setFont(QFont('Arial', 12))
        self.axial_stress_label.move(450, 250)
        self.axial_stress_label.adjustSize()

        self.picture = QLabel(self)
        self.picture.setPixmap(QPixmap("pressure"))
        self.picture.show()
        self.picture.resize(700, 700)
        self.picture.move(450, 250)

    def confirm_button(self):
        self.p_outer = self.outer_pressure.value()
        self.p_inner = self.inner_pressure.value()
        self.d_inner = self.inner_diameter.value()
        self.d_outer = self.outer_diameter.value()

        surface_index = self.surface_cb.currentIndex()
        if surface_index == 0:
            self.surface = False
        if surface_index == 1:
            self.surface = True

        capped_index = self.capped_cb.currentIndex()
        if capped_index == 0:
            self.capped = True
        if capped_index == 1:
            self.capped = False

        self.tangential_stress = PressureVesselStress(self.surface, self.capped, self.p_outer, self.p_inner,
                                                      self.d_outer, self.d_inner).stress_t
        self.radial_stress = PressureVesselStress(self.surface, self.capped, self.p_outer, self.p_inner, self.d_outer,
                                                  self.d_inner).stress_r
        self.axial_stress = PressureVesselStress(self.surface, self.capped, self.p_outer, self.p_inner, self.d_outer,
                                                 self.d_inner).stress_a

        self.tangential_stress_label.setText(f'Tangential Stress: {round(float(self.tangential_stress), 2)} Pa (N/m^2)')
        self.radial_stress_label.setText(f'Radial Stress : {round(float(self.radial_stress), 2)} Pa (N/m^2)')
        self.axial_stress_label.setText(f'Axial Stress : {round(float(self.axial_stress), 2)} Pa (N/m^2)')

        self.tangential_stress_label.adjustSize()
        self.radial_stress_label.adjustSize()
        self.axial_stress_label.adjustSize()


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

    app = QApplication(sys.argv)
    w = PVSWindow()
    w.show()
    sys.exit(app.exec_())