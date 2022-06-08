import numpy as np
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class PSWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Principal Stresses 2D')
        self.x = 1000  # GUI size parameters
        self.y = 1000
        self.width = 900
        self.height = 830
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.sigma_x = None
        self.sigma_y = None
        self.tau_xy = None
        self.avg_norm_stress = None
        self.ps_1 = None
        self.ps_2 = None
        self.ang_ps_1 = None
        self.ang_ps_2 = None
        self.m_shear = None
        self.ang_shear1 = None
        self.ang_shear2 = None

        self.sigma_x_label = QLabel('Stress in the x axis (horizontal right is positive) (MPa)', self)
        self.sigma_x_label.setFont(QFont('Arial', 12))
        self.sigma_x_label.adjustSize()
        self.sigma_x_label.move(50, 150)

        self.sigma_y_label = QLabel('Stress in they axis (vertical up is positive) (MPa)', self)
        self.sigma_y_label.setFont(QFont('Arial', 12))
        self.sigma_y_label.adjustSize()
        self.sigma_y_label.move(50, 200)

        self.tau_xy_label = QLabel('Shear Stress (MPa)', self)
        self.tau_xy_label.setFont(QFont('Arial', 12))
        self.tau_xy_label.adjustSize()
        self.tau_xy_label.move(50, 250)

        self.force_x = QDoubleSpinBox(self)
        self.force_x.setRange(-999999999, 999999999)
        self.force_x.setFont(QFont('Arial', 12))
        self.force_x.move(500, 150)
        self.force_x.adjustSize()

        self.force_y = QDoubleSpinBox(self)
        self.force_y.setRange(-999999999, 999999999)
        self.force_y.setFont(QFont('Arial', 12))
        self.force_y.move(500, 200)
        self.force_y.adjustSize()

        self.shear = QDoubleSpinBox(self)
        self.shear.setRange(-999999999, 999999999)
        self.shear.setFont(QFont('Arial', 12))
        self.shear.move(500, 250)
        self.shear.adjustSize()

        self.confirm_btn = QPushButton('Confirm', self)
        self.confirm_btn.setFont(QFont('Arial', 12))
        self.confirm_btn.setEnabled(True)
        self.confirm_btn.clicked.connect(self.confirm_button)
        self.confirm_btn.move(300, 330)
        self.confirm_btn.adjustSize()

        self.avg_norm_stress_label = QLabel('Average Normal Stress:', self)
        self.avg_norm_stress_label.setFont(QFont('Arial', 12))
        self.avg_norm_stress_label.move(50, 400)
        self.avg_norm_stress_label.adjustSize()

        self.principal_stress_1_label = QLabel('Principal Stress 1:', self)
        self.principal_stress_1_label.setFont(QFont('Arial', 12))
        self.principal_stress_1_label.move(50, 450)
        self.principal_stress_1_label.adjustSize()

        self.principal_stress_2_label = QLabel('Principal Stress 2:', self)
        self.principal_stress_2_label.setFont(QFont('Arial', 12))
        self.principal_stress_2_label.move(50, 500)
        self.principal_stress_2_label.adjustSize()

        self.ang_to_principal_stress_1_label = QLabel('Angle to Reach Principal Stress 1:', self)
        self.ang_to_principal_stress_1_label.setFont(QFont('Arial', 12))
        self.ang_to_principal_stress_1_label.move(50, 550)
        self.ang_to_principal_stress_1_label.adjustSize()

        self.ang_to_principal_stress_2_label = QLabel('Angle to Reach Principal Stress 2:', self)
        self.ang_to_principal_stress_2_label.setFont(QFont('Arial', 12))
        self.ang_to_principal_stress_2_label.move(50, 600)
        self.ang_to_principal_stress_2_label.adjustSize()

        self.max_shear_label = QLabel('Maximum Shear Stress:', self)
        self.max_shear_label.setFont(QFont('Arial', 12))
        self.max_shear_label.move(50, 650)
        self.max_shear_label.adjustSize()

        self.ang_to_max_shear_1_label = QLabel('Angle to Reach Maximum Shear Stress 1:', self)
        self.ang_to_max_shear_1_label.setFont(QFont('Arial', 12))
        self.ang_to_max_shear_1_label.move(50, 700)
        self.ang_to_max_shear_1_label.adjustSize()

        self.ang_to_max_shear_2_label = QLabel('Angle to Reach Maximum Shear Stress 2:', self)
        self.ang_to_max_shear_2_label.setFont(QFont('Arial', 12))
        self.ang_to_max_shear_2_label.move(50, 750)
        self.ang_to_max_shear_2_label.adjustSize()

        self.picture = QLabel(self)
        self.picture.setPixmap(QPixmap("principal"))
        self.picture.show()
        self.picture.resize(700, 700)
        self.picture.move(500, 300)

    def confirm_button(self):
        self.sigma_x = self.force_x.value()
        self.sigma_y = self.force_y.value()
        self.tau_xy = self.shear.value()

        self.avg_norm_stress = PrincipalStresses(self.sigma_x, self.sigma_y, self.tau_xy).s_avg
        self.ps_1 = PrincipalStresses(self.sigma_x, self.sigma_y, self.tau_xy).s1
        self.ps_2 = PrincipalStresses(self.sigma_x, self.sigma_y, self.tau_xy).s2
        self.ang_ps_1 = PrincipalStresses(self.sigma_x, self.sigma_y, self.tau_xy).phi1
        self.ang_ps_2 = PrincipalStresses(self.sigma_x, self.sigma_y, self.tau_xy).phi2
        self.m_shear = PrincipalStresses(self.sigma_x, self.sigma_y, self.tau_xy).t_max
        self.ang_shear1 = PrincipalStresses(self.sigma_x, self.sigma_y, self.tau_xy).shear_phi1
        self.ang_shear2 = PrincipalStresses(self.sigma_x, self.sigma_y, self.tau_xy).shear_phi2

        self.avg_norm_stress_label.setText(f'Average Normal Stress: {round(self.avg_norm_stress, 2)} MPa')
        self.principal_stress_1_label.setText(f'Principal Stress 1: {round(self.ps_1, 2)} MPa')
        self.principal_stress_2_label.setText(f'Principal Stress 2: {round(self.ps_2, 2)} MPa')
        self.ang_to_principal_stress_1_label.setText(f'Angle to Reach Principal Stress 1: {round(self.ang_ps_1, 2)} '
                                                     f'{d}')
        self.ang_to_principal_stress_2_label.setText(f'Angle to Reach Principal Stress 2: {round(self.ang_ps_2, 2)} '
                                                     f'{d}')
        self.max_shear_label.setText(f'Maximum Shear Stress: {round(self.m_shear, 2)} MPa')
        self.ang_to_max_shear_1_label.setText(f'Angle to Reach Maximum Shear Stress 1: {round(self.ang_shear1, 2)} '
                                              f'{d}')
        self.ang_to_max_shear_2_label.setText(f'Angle to Reach Maximum Shear Stress 2: {round(self.ang_shear2, 2)} '
                                              f'{d}')

        self.avg_norm_stress_label.adjustSize()
        self.principal_stress_1_label.adjustSize()
        self.principal_stress_2_label.adjustSize()
        self.ang_to_principal_stress_1_label.adjustSize()
        self.ang_to_principal_stress_2_label.adjustSize()
        self.max_shear_label.adjustSize()
        self.ang_to_max_shear_1_label.adjustSize()
        self.ang_to_max_shear_2_label.adjustSize()


class PrincipalStresses:
    def __init__(self, sigma_x, sigma_y, tau_xy):
        """

        :param sigma_x: stress in x axis (horizontal right is positive)
        :param sigma_y: stress in y axis (vertical up is positive)
        :param tau_xy:  shear
        """
        self.sx = sigma_x
        self.sy = sigma_y
        self.s_avg = (self.sx + self.sy) / 2
        self.txy = tau_xy
        self.s1 = (self.s_avg + math.sqrt((((self.sx - self.sy) / 2) ** 2) + (self.txy ** 2)))
        self.s2 = (self.s_avg - math.sqrt((((self.sx - self.sy) / 2) ** 2) + (self.txy ** 2)))

        self.phi1 = math.degrees(math.atan(self.txy / ((self.sx - self.sy) / 2))) / 2
        self.ccw = self.rotation(self.phi1)
        self.phi2 = self.phi1 + 90
        self.theta1 = self.phi1 * 2
        self.theta2 = self.phi2 * 2
        self.sx_prime = None
        self.sigma_x_prime(self.phi1)
        self.confirm_angle = self.stress_angle_relation()

        # In=plane shear stress
        self.t_max = math.sqrt((((self.sx - self.sy) / 2) ** 2) + (self.txy ** 2))
        self.shear_phi1 = math.degrees(math.atan(-(((self.sx - self.sy) / 2) / self.txy))) / 2
        self.shear_ccw = self.shear_direction(self.shear_phi1)
        self.shear_phi2 = self.shear_phi1 + 90

        # print(f'Average Normal Stress = {self.s_avg}')
        # print(f'Principal Stress 1 = {self.s1}')
        # print(f'Principal Stress 2 = {self.s2}')
        # print(f'Angle to Reach Principal Stress 1 = {self.phi1}')
        # print(f'Angle to Reach Principal Stress 2 = {self.phi2}')
        # print(f'Maximum Shear Stress = {self.t_max}')
        # print(f'Angle to Reach Max Shear Stress 1 = {self.shear_phi1}')
        # print(f'Angle to Reach Max Shear Stress 2 = {self.shear_phi2}')

    def rotation(self, angle):
        return angle > 0

    def shear_direction(self, angle):
        return angle > 0

    def sigma_x_prime(self, angle):
        rad_angle = math.radians(angle)
        self.sx_prime = ((self.sx + self.sy) / 2) + (((self.sx - self.sy) / 2) * math.cos(2 * rad_angle)) + (self.txy * math.sin(2 * rad_angle))

    def stress_angle_relation(self):
        return (self.s1 - self.sx_prime) == 0


if __name__ == "__main__":
    pi = math.pi
    d = u"\u00b0"
    app = QApplication(sys.argv)
    w = PSWindow()
    w.show()
    sys.exit(app.exec_())