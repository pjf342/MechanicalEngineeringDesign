import numpy as np
import math
import sys


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
    # PS = PrincipalStresses(2,2,3)
