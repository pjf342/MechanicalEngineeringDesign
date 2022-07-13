import math


class ColumnHollowRectangle:
    def __init__(self, b, h, t, L, sy, e, bc, vt):
        super().__init__()
        """
        
        :param b: base (mm)
        :type b float
        :param h: height (mm)
        :type h float
        :param t: thickness (mm)
        :type t float
        :param L: length of column (m)
        :type L float
        :param sy: yield strength (MPa)
        :type sy float
        :param e: modulus of elasticity (GPa)
        :type e float
        :param bc: boundary condition: 0:fixed-free, 1:rounded-rounded, 2:fixed-rounded, 3:fixed-fixed
        :type bc int
        :param vt: end condition value type: 0:theoretical value, 1:conservative value, 2:recommended value
        :type vt int
        """
        self.b = b / 1000  # converts from mm to m
        self.h = h / 1000  # converts from mm to m
        self.t = t / 1000  # converts from mm to m
        self.bi = self.b - (self.t * 2)  # inner base
        self.hi = self.h - (self.t * 2)  # inner height
        self.L = L  # column length
        self.sy = sy * 1000000  # Converts to Pa
        self.e = e * 1000000000  # Converts to Pa
        self.c = c_table(bc, vt)
        self.lk1 = ((2 * (pi ** 2) * self.c * self.e) / self.sy) ** .5  # determining slenderness
        self.Ix = ((self.b * (self.h ** 3)) / 12) - ((self.bi * (self.hi ** 3)) / 12)  # area moment of inertia, x axis
        self.Iy = ((self.h * (self.b ** 3)) / 12) - ((self.hi * (self.bi ** 3)) / 12)  # area moment of inertia, y axis
        self.Imin = min(self.Ix, self.Iy)
        self.A = (self.b * self.h) - (self.bi * self.hi)  # area of hollow rectangle
        self.k = (self.Imin / self.A) ** .5  # radius of gyration
        self.sr = self.L / self.k
        self.technique = technique_determination(self.sr, self.lk1)
        self.scr = None  # sigma critical (Pa)
        self.pcr = None  # critical load (N)
        self.technique_determination()
        self.N = self.sy / self.scr

    def technique_determination(self):
        if self.technique == 0:
            self.scr = (self.c * self.e * (pi ** 2)) / (self.sr ** 2)
            self.pcr = self.scr * self.A
        else:
            self.scr = self.sy - (1 / (self.c * self.e)) * ((self.sy * self.L) / (2 * pi * self.k)) ** 2
            self.pcr = self.scr * self.A


class ColumnSolidRectangle:
    def __init__(self, b, h, L, sy, e, bc, vt):
        super().__init__()
        """

        :param b: base (mm)
        :type b float
        :param h: height (mm)
        :type h float
        :param L: length of column (m)
        :type L float
        :param sy: yield strength (MPa)
        :type sy float
        :param e: modulus of elasticity (GPa)
        :type e float
        :param bc: boundary condition: 0:fixed-free, 1:rounded-rounded, 2:fixed-rounded, 3:fixed-fixed
        :type bc int
        :param vt: end condition value type: 0:theoretical value, 1:conservative value, 2:recommended value
        :type vt int
        """
        self.b = b / 1000  # converts from mm to m
        self.h = h / 1000  # converts from mm to m
        self.L = L  # column length
        self.sy = sy * 1000000  # Converts to Pa
        self.e = e * 1000000000  # Converts to Pa
        self.c = c_table(bc, vt)
        self.lk1 = ((2 * (pi ** 2) * self.c * self.e) / self.sy) ** .5  # determining slenderness
        self.Ix = ((self.b * (self.h ** 3)) / 12)  # area moment of inertia, x axis
        self.Iy = ((self.h * (self.b ** 3)) / 12)  # area moment of inertia, y axis
        self.Imin = min(self.Ix, self.Iy)
        self.A = (self.b * self.h)  # area of hollow rectangle
        self.k = (self.Imin / self.A) ** .5  # radius of gyration
        self.sr = self.L / self.k
        self.technique = technique_determination(self.sr, self.lk1)
        self.scr = None  # sigma critical (Pa)
        self.pcr = None  # critical load (N)
        self.technique_determination()
        self.N = self.sy / self.scr

    def technique_determination(self):
        if self.technique == 0:
            self.scr = (self.c * self.e * (pi ** 2)) / (self.sr ** 2)
            self.pcr = self.scr * self.A
        else:
            self.scr = self.sy - (1 / (self.c * self.e)) * ((self.sy * self.L) / (2 * pi * self.k)) ** 2
            self.pcr = self.scr * self.A


class ColumnHollowCircle:
    def __init__(self, d, t, L, sy, e, bc, vt):
        super().__init__()
        """

        :param d: diameter (mm)
        :type b float
        :param t: thickness (mm)
        :type t float
        :param L: length of column (m)
        :type L float
        :param sy: yield strength (MPa)
        :type sy float
        :param e: modulus of elasticity (GPa)
        :type e float
        :param bc: boundary condition: 0:fixed-free, 1:rounded-rounded, 2:fixed-rounded, 3:fixed-fixed
        :type bc int
        :param vt: end condition value type: 0:theoretical value, 1:conservative value, 2:recommended value
        :type vt int
        """
        self.d = d / 1000  # converts from mm to m
        self.t = t / 1000  # converts from mm to m
        self.di = self.d - (self.t * 2)  # inner diameter
        self.L = L  # column length
        self.sy = sy * 1000000  # Converts to Pa
        self.e = e * 1000000000  # Converts to Pa
        self.c = c_table(bc, vt)
        self.lk1 = ((2 * (pi ** 2) * self.c * self.e) / self.sy) ** .5  # determining slenderness
        self.I = (pi * ((self.d ** 4) - (self.di ** 4))) / 64
        self.A = (pi * ((self.d/2) ** 2)) - (pi * ((self.di/2) ** 2))  # area of hollow circle
        self.k = (self.I / self.A) ** .5  # radius of gyration
        self.sr = self.L / self.k
        self.technique = technique_determination(self.sr, self.lk1)
        self.scr = None  # sigma critical (Pa)
        self.pcr = None  # critical load (N)
        self.technique_determination()
        self.N = self.sy / self.scr

    def technique_determination(self):
        if self.technique == 0:
            self.scr = (self.c * self.e * (pi ** 2)) / (self.sr ** 2)
            self.pcr = self.scr * self.A
        else:
            self.scr = self.sy - (1 / (self.c * self.e)) * ((self.sy * self.L) / (2 * pi * self.k)) ** 2
            self.pcr = self.scr * self.A


class ColumnSolidCircle:
    def __init__(self, d, L, sy, e, bc, vt):
        super().__init__()
        """

        :param d: diameter (mm)
        :type b float
        :param L: length of column (m)
        :type L float
        :param sy: yield strength (MPa)
        :type sy float
        :param e: modulus of elasticity (GPa)
        :type e float
        :param bc: boundary condition: 0:fixed-free, 1:rounded-rounded, 2:fixed-rounded, 3:fixed-fixed
        :type bc int
        :param vt: end condition value type: 0:theoretical value, 1:conservative value, 2:recommended value
        :type vt int
        """
        self.d = d / 1000  # converts from mm to m
        self.L = L  # column length
        self.sy = sy * 1000000  # Converts to Pa
        self.e = e * 1000000000  # Converts to Pa
        self.c = c_table(bc, vt)
        self.lk1 = ((2 * (pi ** 2) * self.c * self.e) / self.sy) ** .5  # determining slenderness
        self.I = (pi * (self.d ** 4)) / 64
        self.A = pi * ((self.d/2) ** 2)  # area of hollow circle
        self.k = (self.I / self.A) ** .5  # radius of gyration
        self.sr = self.L / self.k
        self.technique = technique_determination(self.sr, self.lk1)
        self.scr = None  # sigma critical (Pa)
        self.pcr = None  # critical load (N)
        self.technique_determination()
        self.N = self.sy / self.scr

    def technique_determination(self):
        if self.technique == 0:
            self.scr = (self.c * self.e * (pi ** 2)) / (self.sr ** 2)
            self.pcr = self.scr * self.A
        else:
            self.scr = self.sy - (1 / (self.c * self.e)) * ((self.sy * self.L) / (2 * pi * self.k)) ** 2
            self.pcr = self.scr * self.A


class ColumnSymmetricalIBeam:
    def __init__(self, H, h, a, b, L, sy, e, bc, vt):
        super().__init__()
        """

        :param H: height of I-beam (mm)
        :type H float
        :param h: flange-flange inner face height (mm)
        :type h float
        :param a: width of I-beam web (mm)
        :type a float
        :param b: base of I-beam (mm)
        :type b float
        
        :param L: length of column (m)
        :type L float
        :param sy: yield strength (MPa)
        :type sy float
        :param e: modulus of elasticity (GPa)
        :type e float
        :param bc: boundary condition: 0:fixed-free, 1:rounded-rounded, 2:fixed-rounded, 3:fixed-fixed
        :type bc int
        :param vt: end condition value type: 0:theoretical value, 1:conservative value, 2:recommended value
        :type vt int
        """
        self.H = H / 1000  # converts from mm to m
        self.h = h / 1000  # converts from mm to m
        self.a = a / 1000  # converts from mm to m
        self.b = b / 1000  # converts from mm to m
        self.L = L  # column length
        self.sy = sy * 1000000  # Converts to Pa
        self.e = e * 1000000000  # Converts to Pa
        self.c = c_table(bc, vt)
        self.lk1 = ((2 * (pi ** 2) * self.c * self.e) / self.sy) ** .5  # determining slenderness
        self.Ix = (self.a * (self.h ** 3) / 12) + ((self.b / 12) * ((self.H ** 3) - (self.h ** 3)))
        self.Iy = (self.h * (self.a ** 3) / 12) + (((self.b ** 3) / 12) * (self.H - self.h))
        self.Imin = min(self.Ix, self.Iy)
        self.A = (2 * self.b * ((self.H - self.h) / 2)) + (self.h * self.a)

        self.k = (self.Imin / self.A) ** .5  # radius of gyration
        self.sr = self.L / self.k
        self.technique = technique_determination(self.sr, self.lk1)
        self.scr = None  # sigma critical (Pa)
        self.pcr = None  # critical load (N)
        self.technique_determination()
        self.N = self.sy / self.scr
        print(self.A)

    def technique_determination(self):
        if self.technique == 0:
            self.scr = (self.c * self.e * (pi ** 2)) / (self.sr ** 2)
            self.pcr = self.scr * self.A
        else:
            self.scr = self.sy - (1 / (self.c * self.e)) * ((self.sy * self.L) / (2 * pi * self.k)) ** 2
            self.pcr = self.scr * self.A


if __name__ == "__main__":
    def c_table(column_end_condition, value_type):
        if column_end_condition == 0:
            value = [.25, .25, .25]
        if column_end_condition == 1:
            value = [1, 1, 1]
        if column_end_condition == 2:
            value = [2, 1, 1.2]
        if column_end_condition == 3:
            value = [4, 1, 1.2]
        return value[value_type]

    def technique_determination(slenderness_ratio, determining_slenderness):  # 0 : euler, 1 : johnson
        return 0 if slenderness_ratio > determining_slenderness else 1


    pi = math.pi





