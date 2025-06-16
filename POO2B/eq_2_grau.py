from math import sqrt

class Eq_2_grau:

    def __init__(self, a, b ,c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    def set_a(self, v):
        if v == 0:
            raise ValueError("O valor de A não pode ser 0!")
        else:
            self.__a = v

    def get_a(self):
        return self.__a
    
    def set_b(self, v):
        self.__b = v

    def get_b(self):
        return self.__b
    
    def set_c(self, v):
       self.__c = v

    def get_c(self):
        return self.__c
    
    def delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
    
    def mais_delta(self):
        return (-self.__b + sqrt(self.delta())) / 2 * self.__a
    
    def menos_delta(self):
        return (-self.__b - sqrt(self.delta())) / 2 * self.__a
    
    def __str__(self):
        return f"Valores da equação: A: {self.__a}; B: {self.__b}; C:{self.__c}"