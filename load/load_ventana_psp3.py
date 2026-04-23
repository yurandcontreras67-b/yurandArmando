from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from psp.ejercicio3.psp3 import PSP3


class VentanaPSP3(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp_3.ui", self)

        self.BTN_CALCULAR.clicked.connect(self.calcular)

    def calcular(self):
        dof = int(self.TXT_DOF.text())
        p = float(self.TXT_P.text())
        x = float(self.TXT_X.text())

        modelo = PSP3(x, dof, p)
        resultado = modelo.calcular()

        self.LABEL_RESULTADOS.setText(str(round(resultado, 6)))