import math

#o sublinhado __ é uma marca de encapsulamento, qualquer valor atribuído a váriaveis com essas marcas
#não poderá ser acessado por outras classes

class Triangulo:
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
        return self.__b * self.__h / 2
    pass

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

class UI:
    @staticmethod
    def menu():
        print("Selecione uma figura: 1-Triângulo, 2-Retângulo, 3-Círculo, 10-Fim")
        return int(input())
    
    @staticmethod
    def main():
        op=0
        while op!=10:
            op=UI.menu()
            if op==1:  
                UI.triangulo()
            elif op==2:
                UI.retangulo()
            elif op==3:
                UI.circulo()

    @staticmethod        
    def triangulo():
        x=Triangulo()
        x.set_base(float(input("Digite a base do triângulo: ")))
        x.set_altura(float(input("Digite a altura do triângulo: ")))

        print()

        print(f"Base do triângulo: {x.get_base():.2f}")
        print(f"Altura do triângulo: {x.get_altura():.2f}")
        print(f"Área do triângulo: {x.calc_area():.2f}")
        
    @staticmethod
    def retangulo():
        x=Retangulo()

        x.set_base(float(input("Digite a base do retângulo: ")))
        x.set_altura(float(input("Digite a altura do retângulo: ")))

        print()

        print(f"Base do retângulo: {x.get_base():.2f}")
        print(f"Altura do retângulo: {x.get_altura():.2f}")
        print(f"Área do retângulo: {x.calc_area():.2f}")

    @staticmethod
    def circulo():
        x=Circulo()

        x.set_raio(float(input("Digite o raio do círculo: ")))

        print()

        print(f"Raio do círculo: {x.get_raio():.2f}")
        print(f"Área do círculo: {x.calc_area():.2f}")    

    pass

UI.main()