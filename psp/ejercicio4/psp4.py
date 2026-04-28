from psp.ejercicio3.psp3 import PSP3
from psp.ejercicio1.psp1 import PSP1
import math


class PSP4(PSP3):
    def __init__(self, x, y, xk, p, n):
        self.x = x
        self.y = y
        self.xk = xk
        self.p = p
        self.n = n

    def calcular(self):
        x = self.x[:self.n]
        y = self.y[:self.n]
        n = self.n

        modelo_psp1 = PSP1(x, y)
        res1 = modelo_psp1.calcular()

        b0 = res1["b0"]
        b1 = res1["b1"]
        r = res1["r"]
        r2 = res1["r2"]

       
        yk = b0 + b1 * self.xk
        x_avg = sum(x) / n

    
        suma = 0
        for i in range(n):
            suma += (y[i] - b0 - b1 * x[i]) ** 2
            
        sigma = math.sqrt(suma / (n - 2))
        dof = n - 2

        
        super().__init__(1, dof, self.p)
        t = super().calcular()
        den = sum((x[i] - x_avg) ** 2 for i in range(n))
        rango = t * sigma * math.sqrt(1 + (1 / n) + ((self.xk - x_avg) ** 2 / den))

        upi = yk + rango
        lpi = yk - rango

        return {
            "b0": b0,
            "b1": b1,
            "r": r,
            "r2": r2,
            "yk": yk,
            "tail": self.p,
            "rango": rango,
            "upi": upi,
            "lpi": lpi
        }