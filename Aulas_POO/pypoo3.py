import circulo, triangulo, retangulo

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
        x=triangulo.Triangulo()
        x.set_base(float(input("Digite a base do triângulo: ")))
        x.set_altura(float(input("Digite a altura do triângulo: ")))

        print()

        print(f"Base do triângulo: {x.get_base():.2f}")
        print(f"Altura do triângulo: {x.get_altura():.2f}")
        print(f"Área do triângulo: {x.calc_area():.2f}")
        
    @staticmethod
    def retangulo():
        x=retangulo.Retangulo()

        x.set_base(float(input("Digite a base do retângulo: ")))
        x.set_altura(float(input("Digite a altura do retângulo: ")))

        print()

        print(f"Base do retângulo: {x.get_base():.2f}")
        print(f"Altura do retângulo: {x.get_altura():.2f}")
        print(f"Área do retângulo: {x.calc_area():.2f}")

    @staticmethod
    def circulo():
        x=circulo.Circulo()

        x.set_raio(float(input("Digite o raio do círculo: ")))

        print()

        print(f"Raio do círculo: {x.get_raio():.2f}")
        print(f"Área do círculo: {x.calc_area():.2f}")    

    pass

UI.main()