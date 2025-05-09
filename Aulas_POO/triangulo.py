class Triangulo:
    def __init__(self): #def __init__(self, b, h):
        """
        #opção 1 repetir o códgio set
        if b>0:
            self.__b=b
        else:
            raise ValueError("A base deve ser positiva")
        #opção 2 chamar o método set
        self.set_altura(self, h)
        """
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
        return self.__b * self.__h / 2
    
    def __str__(self):
        return "Olá, eu calculo a área de um triângulo!"

    pass