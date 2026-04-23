from psp.ejercicio2.psp2 import PSP2

class PSP3:
    def __init__(self, x, dof, p, tolerancia=0.00001):
        self.x = x
        self.dof = dof
        self.p = p
        self.tolerancia = tolerancia
        self.pCalculada = 0  
        
    def funcion(self, x):
        modelo = PSP2(x, self.dof)
        return modelo.calcular()

    def calcular(self):
        x = self.x
        d = 0.5
        error_signo_anterior = None

        while True:
            self.pCalculada = self.funcion(x)

            error_signo = self.p - self.pCalculada
            error_sin_signo = abs(error_signo)

            if error_sin_signo < self.tolerancia:
                break

            if error_signo_anterior is not None:
                if error_signo * error_signo_anterior < 0:
                    d = d / 2

            if self.pCalculada < self.p:
                x = x + d
            else:
                x = x - d

            error_signo_anterior = error_signo

        return x