from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from psp.ejercicio2.psp2 import PSP2


class VentanaPSP2(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp_2.ui", self)

        self.btn_calcular.clicked.connect(self.calcular)

    def calcular(self):
        dof = int(self.txt_dof.text())
        x = float(self.txt_x.text())

        modelo = PSP2(x, dof)
        resultado = modelo.calcular()

        self.label_resultado.setText(str(round(resultado, 6)))