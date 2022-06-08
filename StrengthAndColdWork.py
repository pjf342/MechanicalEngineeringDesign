import numpy as np
import math
import sys


class Tables:
    def __init__(self):
        # col1 | 0=steel, 1=stainless steel, 2=aluminum alloy
        # col2 | 0=annealed, 1=HR, 2=Q&T 600F, 3=T6, 4=T4,
        # col3 | Yield (MPa)
        # col4 | Ultimate (MPa)
        # col5 | Fracture (MPa)
        # col6 | Coefficient (MPa)
        # col7 | Strain Strength (Exponent)
        # col8 | Fracture Strain
        self.Table_A_22 = np.array([[1018, 1144, 1212, 1045, 4142, 303, 304, 2011, 2024, 7075],
                                    [0, 0, 0, 0, 0, 1, 1, 2, 2, 2],
                                    [0, 0, 1, 2, 2, 0, 0, 3, 4, 3],
                                    [220, 358, 193, 1520, 1720, 241, 276, 169, 296, 542],
                                    [341, 646, 424, 1580, 1930, 601, 568, 324, 446, 593],
                                    [628, 898, 729, 2380, 2340, 1520, 1600, 325, 533, 706],
                                    [620, 992, 758, 1880, 1760, 1410, 1270, 620, 689, 882],
                                    [.25, .14, .24, .041, .048, .51, .45, .28, .15, .13],
                                    [1.05, .49, .85, .81, .43, 1.16, 1.67, .1, .18, .18]])

    def switch_material(self, index):
        switch = {
            0: 'Steel',
            1: 'Stainless Steel',
            2: 'Aluminum Alloy'
        }
        return switch.get(int(index), "Invalid Material")

    def switch_condition(self, index):
        switch = {
            0: 'Annealed',
            1: 'HR',
            2: 'Q&T 600F',
            3: 'T6',
            4: 'T4'
        }
        return switch.get(int(index), "Invalid Condition")


class StrengthAndColdWork:
    def __init__(self, material_number, cold_work_percent):
        super().__init__()
        """

        :param material_number: The material number (Ex: 304-Aluminum = 304)
        :param cold_work_percent: Cold work percentage (percentage form, not decimal form. Ex: 25% = 25)
        :type material_number: int
        :type cold_work_percent: int
        """
        self.index = None
        self.number = material_number  # col0
        self.material = None
        self.condition = None
        self.yield_str = None
        self.ultimate = None
        self.fracture = None
        self.coefficient = None
        self.strain_str = None
        self.fracture_strain = None

        self.cold_work_percent = (cold_work_percent / 100)
        self.new_yield = None
        self.new_ultimate = None
        self.true_strain = None

        self.obtain_index()
        self.new_yield_and_ultimate_strength()

        # print(self.new_yield, self.new_ultimate, self.true_strain)

    def obtain_index(self):
        self.index = np.where(tab.Table_A_22[0] == self.number)
        self.material = tab.switch_material(tab.Table_A_22[1][self.index])
        self.condition = tab.switch_condition(tab.Table_A_22[2][self.index])
        self.yield_str = tab.Table_A_22[3][self.index]
        self.ultimate = tab.Table_A_22[4][self.index]
        self.fracture = tab.Table_A_22[5][self.index]
        self.coefficient = tab.Table_A_22[6][self.index]
        self.strain_str = tab.Table_A_22[7][self.index]
        self.fracture_strain = tab.Table_A_22[8][self.index]

    def new_yield_and_ultimate_strength(self):
        self.true_strain = math.log(1/(1 - self.cold_work_percent))
        self.new_yield = self.coefficient * self.true_strain ** self.strain_str
        self.new_ultimate = self.ultimate / (1 - self.cold_work_percent)


if __name__ == "__main__":
    pi = math.pi
    tab = Tables()


