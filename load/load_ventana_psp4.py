from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from psp.ejercicio4.psp4 import PSP4


class VentanaPSP4(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp_4.ui", self)

        self.btn_calcular.clicked.connect(self.calcular)
        self.btn_caso1.clicked.connect(self.caso1)

    def caso1(self):
        self.caso = 1

    def calcular(self):

            if self.caso == 1:
                x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
                y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
                p = 0.35
            
            n = int(self.edit_n.text())
            xk = float(self.edit_xk.text())

            modelo = PSP4(x, y, xk, p, n)
            resultado = modelo.calcular()

            self.label_B1_2.setText(str(round(resultado["b1"], 3)))
            self.label_B0_2.setText(str(round(resultado["b0"], 3)))
            self.label_r_2.setText(str(round(resultado["r"], 3)))
            self.label_r2_2.setText(str(round(resultado["r2"], 3)))
            self.label_yk_2.setText(str(round(resultado["yk"], 3)))

            self.label_taile.setText(str(round(resultado["tail"], 3)))
            self.label_range.setText(str(round(resultado["rango"], 3)))
            self.label_UPI.setText(str(round(resultado["upi"], 3)))
            self.label_LPI.setText(str(round(resultado["lpi"], 3)))

        