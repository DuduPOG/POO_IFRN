class Retangulo:
    def __init__(self):
        self.__b=0 
        self.__h=0

    def set_base(self, v):
        if v>0:
            self.__b=v
        else:
            raise ValueError("A base deve ser positiva")

    def set_altura(self, v):
        if v>0:
            self.__h=v
        else:
            raise ValueError("A altura deve ser positiva")

    def get_base(self):
        return self.__b
    
    def get_altura(self):
        return self.__h    

    def calc_area(self):
        return self.__b * self.__h
    pass