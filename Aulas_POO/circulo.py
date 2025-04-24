import math

class Circulo:
    def __init__(self):
        self.__r=0

    def set_raio(self, v):
        if v>0:
            self.__r=v
        else:
            raise ValueError("O raio deve ser positivo")

    def get_raio(self):
        return self.__r
    
    def calc_area(self):
        return math.pi*self.__r**2
    pass