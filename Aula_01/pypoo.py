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

#testando a classe, x é a referência dos objetos da classe
x=Triangulo()

#base do triângulo
x.b=float(input())

#altura do triângulo
x.h=float(input())

print(f"Base do triângulo: {x.b:.2f}")
print(f"Altura do triângulo: {x.h:.2f}")
print(f"Área do triângulo: {x.calc_area():.2f}")