from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from load.load_ventana_psp1 import VentanaPSP1
from load.load_ventana_psp2 import VentanaPSP2
from load.load_ventana_psp3 import VentanaPSP3
from load.load_ventana_psp4 import VentanaPSP4


class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_menu.ui", self)

        self.btn_psp1.triggered.connect(self.abrir_psp1)
        self.btn_psp2.triggered.connect(self.abrir_psp2)
        self.btn_psp3.triggered.connect(self.abrir_psp3)
        self.btn_psp4.triggered.connect(self.abrir_psp4)
        self.btn_salir.triggered.connect(self.close)

    def abrir_psp1(self):
        self.ventana_psp1 = VentanaPSP1()
        self.ventana_psp1.exec_()

    def abrir_psp2(self):
        self.ventana_psp2 = VentanaPSP2()
        self.ventana_psp2.exec_()
    
    def abrir_psp3(self):
        self.ventana_psp3 = VentanaPSP3()
        self.ventana_psp3.exec_()
        
    def abrir_psp4(self):
        self.ventana_psp3 = VentanaPSP4()
        self.ventana_psp3.exec_()