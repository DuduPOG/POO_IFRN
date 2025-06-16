from math import sqrt
class Retangulo:
    def __init__(self, b, h):
        self.set_base(b)
        self.set_altura(h)

    def set_base(self, v):
        if v > 0:
            self.__b = v
        else:
            raise ValueError("A base deve ser positiva")

    def set_altura(self, v):
        if v > 0:
            self.__h = v
        else:
            raise ValueError("A altura deve ser positiva")

    def get_base(self):
        return self.__b
    
    def get_altura(self):
        return self.__h    

    def calc_area(self):
        return self.__b * self.__h
    
    def calc_diagonal(self):
        return sqrt(self.__b ** 2 + self.__h ** 2)
    
    def __str__(self):
        return f"Base do retângulo: {self.__b} - Altura do retângulo: {self.__h}"
    
    pass