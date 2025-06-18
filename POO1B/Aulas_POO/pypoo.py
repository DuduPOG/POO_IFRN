class Triangulo: #classe que calcula a área de um triângulo qualquer

#método que define os valores necessários para o cálculo
    def __init__(self):
        self.b=0 #valor padrão = valor inicial do campo/atributo
        self.h=0

#método que realiza o cálculo da área
    def calc_area(self):
        return self.b * self.h / 2
    
#o self é usado para o python saber quais valores da classe serão usados
            
    pass #fim da classe

#instância = objeto

#forma de organizar o programa para que o usuário só interaja numa parte específica
class UI:
    @staticmethod #isso possibilita que a classe não precise de um objeto
    def main():
        x=Triangulo()

        #base do triângulo
        x.b=float(input())

        #altura do triângulo
        x.h=float(input())

        print(f"Base do triângulo: {x.b:.2f}")
        print(f"Altura do triângulo: {x.h:.2f}")
        print(f"Área do triângulo: {x.calc_area():.2f}")
    pass

UI.main()
#também pode se usar uma referência: u=UI.main(); u.main()