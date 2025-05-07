import random
class Bingo:
    def __init__(self,num_bolas,lista):
        self.__num_bolas=int(num_bolas)
        self.__bolas=lista
        self.__sorteadas=[]

    def proximo(self,x):
        y=random.choice(self.__bolas)
        self.__bolas.remove(y)
        self.__sorteadas.append(y)
        return y
        

    def sorteadas(self, y):
        self.__sorteadas.append(y)
        return self.__sorteadas

    def __str__(self):
        return f"Estas foram as bolas sorteadas: {self.__sorteadas}"    
        
    pass


bolas=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(Bingo(10,bolas))