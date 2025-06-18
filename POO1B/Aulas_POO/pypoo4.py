import math
class Retangulo:
    def __init__(self): #def __init__(self, b, h):
        """
        #opção 1 repetir o códgio set
        if b>0:
            self.__b=b
        else:
            raise ValueError("A base deve ser positiva")
        #opção 2 chamar o método set
        self.set_altura(h)
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
        return self.__b * self.__h
    
    def calc_diagonal(self):
        return math.sqrt(math.pow(self.__b,2)+math.pow(self.__h,2))
    
    def __str__(self):
        return f"Olá, eu calculo a área e a diagonal de um retângulo com os valores da base: {self.__b} e altura {self.__h} fornecidos por você!"

    pass

class UI:
    @staticmethod
    def menu():
        print("Você quer executar o programa?: 1-Sim, 10-Não")
        return int(input())
    
    @staticmethod
    def main():
        op=0
        while op!=10 and op!=1:
            op=UI.menu()
            if op==1:  
                UI.retangulo()
        
    @staticmethod
    def retangulo():
        x=Retangulo()

        x.set_base(float(input("Digite a base do retângulo: ")))
        x.set_altura(float(input("Digite a altura do retângulo: ")))

        print()
        print(x)
        print()

        print(f"Base do retângulo: {x.get_base():.2f}")
        print(f"Altura do retângulo: {x.get_altura():.2f}")
        print(f"Área do retângulo: {x.calc_area():.2f}")
        print(f"Diagonal do retângulo: {x.calc_diagonal():.2f}\n")

    pass

UI.main()