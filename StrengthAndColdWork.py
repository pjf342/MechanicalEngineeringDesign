import numpy as np
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class SCWWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.scw = None
        self.material_number = None
        self.sp_value = None
        self.new_yield = None
        self.new_ultimate = None
        self.true_strain = None
        self.setWindowTitle('Strength and Cold Work - Metric')
        self.x = 1000  # GUI size parameters
        self.y = 1000
        self.width = 700
        self.height = 300
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.info_label1 = QLabel('Cold working puts stress on the material beyond its yield strength to a point in '
                                  'the plastic deformation region', self)
        self.info_label2 = QLabel('and then the load is removed. This increases the ''material\'s yield strength,'
                                  ' however makes the material less', self)
        self.info_label3 = QLabel('ductile and more brittle.', self)

        self.materials_label = QLabel('Material', self)
        self.cold_work_label = QLabel('Cold Work (%)', self)

        self.cb = QComboBox(self)
        self.cb.addItems(['1018 Steel', '1144 Steel', '1212 Steel', '1045 Steel', '4142 Steel', '303 Stainless Steel',
                          '304 Stainless Steel', '2011 Aluminum Alloy', '2024 Aluminum Alloy', '7075 Aluminum Alloy'])

        self.sp = QSpinBox(self)
        self.sp.setRange(0, 99)

        self.confirm_btn = QPushButton('Confirm', self)
        self.confirm_btn.setEnabled(True)
        self.confirm_btn.clicked.connect(self.confirm_button)

        self.new_yield_label = QLabel('New Yield Strength:', self)
        self.new_ultimate_label = QLabel('New Ultimate Strength:', self)
        self.true_strain_label = QLabel('True Strain:', self)

        self.info_label1.setFont(QFont('Arial', 10))
        self.info_label1.adjustSize()
        self.info_label2.setFont(QFont('Arial', 10))
        self.info_label2.adjustSize()
        self.info_label3.setFont(QFont('Arial', 10))
        self.info_label3.adjustSize()
        self.materials_label.setFont(QFont('Arial', 12))
        self.cb.setFont(QFont('Arial', 12))
        self.cold_work_label.setFont(QFont('Arial', 12))
        self.sp.setFont(QFont('Arial', 12))
        self.confirm_btn.setFont(QFont('Arial', 12))
        self.new_yield_label.setFont(QFont('Arial', 12))
        self.new_ultimate_label.setFont(QFont('Arial', 12))
        self.true_strain_label.setFont(QFont('Arial', 12))

        self.info_label1.move(10, 10)
        self.info_label2.move(10, 30)
        self.info_label3.move(10, 50)
        self.materials_label.move(20, 100)
        self.materials_label.adjustSize()
        self.cb.move(170, 100)
        self.cb.adjustSize()
        self.cold_work_label.move(20, 150)
        self.cold_work_label.adjustSize()
        self.sp.move(170, 150)
        self.sp.adjustSize()
        self.confirm_btn.move(100, 200)
        self.confirm_btn.adjustSize()
        self.new_yield_label.move(400, 100)
        self.new_yield_label.adjustSize()
        self.new_ultimate_label.move(400, 150)
        self.new_ultimate_label.adjustSize()
        self.true_strain_label.move(400, 200)
        self.true_strain_label.adjustSize()

    def confirm_button(self):
        self.sp_value = self.sp.value()
        material_index = self.cb.currentIndex()
        if material_index == 0:
            self.material_number = 1018
        if material_index == 1:
            self.material_number = 1144
        if material_index == 2:
            self.material_number = 1212
        if material_index == 3:
            self.material_number = 1045
        if material_index == 4:
            self.material_number = 4142
        if material_index == 5:
            self.material_number = 303
        if material_index == 6:
            self.material_number = 304
        if material_index == 7:
            self.material_number = 2011
        if material_index == 8:
            self.material_number = 2024
        if material_index == 9:
            self.material_number = 7075

        StrengthAndColdWork(self.material_number, self.sp_value)
        self.new_yield = StrengthAndColdWork(self.material_number, self.sp_value).new_yield
        self.new_ultimate = StrengthAndColdWork(self.material_number, self.sp_value).new_ultimate
        self.true_strain = StrengthAndColdWork(self.material_number, self.sp_value).true_strain
        self.new_yield_label.setText(f'New Yield Strength: {round(float(self.new_yield), 2)} MPa')
        self.new_ultimate_label.setText(f'New Ultimate Strength: {round(float(self.new_ultimate), 2)} MPa')
        self.true_strain_label.setText(f'True Strain: {round(float(self.true_strain), 2)}')

        self.materials_label.adjustSize()
        self.cb.adjustSize()
        self.cold_work_label.adjustSize()
        self.sp.adjustSize()
        self.confirm_btn.adjustSize()
        self.new_yield_label.adjustSize()
        self.new_ultimate_label.adjustSize()
        self.true_strain_label.adjustSize()




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
    mat_num = 1018
    cw_percent = 0
    scw = StrengthAndColdWork(mat_num, cw_percent)

    app = QApplication(sys.argv)
    w = SCWWindow()
    w.show()
    sys.exit(app.exec_())
