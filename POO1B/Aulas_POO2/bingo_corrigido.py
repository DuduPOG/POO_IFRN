import random

class Bingo:
    def __init__(self, num_bolas, lista_bolas):
        if num_bolas < 1:
            raise ValueError("O número de bolas deve ser positivo")
        if num_bolas > len(lista_bolas):
            raise ValueError("O número de bolas não pode ser maior que o número de bolas disponíveis")
        self.__num_bolas = int(num_bolas)
        # Cria uma cópia da lista para não modificar a original externamente
        self.__bolas = lista_bolas[:]
        random.shuffle(self.__bolas) # Embaralha as bolas no início
        self.__sorteadas = []
        self.__indice_sorteio = 0 # Controla a próxima bola a ser sorteada

    def proximo(self):
        if self.__indice_sorteio < self.__num_bolas:
            proxima_bola = self.__bolas[self.__indice_sorteio]
            self.__sorteadas.append(proxima_bola)
            self.__indice_sorteio += 1
            return proxima_bola
        else:
            return None # Indica que todas as bolas foram sorteadas

    def todas_sorteadas(self):
        return self.__sorteadas

    def __str__(self):
        return f"Bolas sorteadas até o momento: {self.__sorteadas}"

bolas = list(range(1, 11)) # Uma forma mais concisa de criar a lista de bolas
num_sorteadas = 10
jogo = Bingo(num_sorteadas, bolas)

# Simulação do sorteio

print(f"Lista original de bolas: {bolas}")

for i in range(num_sorteadas + 1): # Tentamos sortear uma vez a mais para testar o None
    bola_sorteada = jogo.proximo()
    if bola_sorteada is None:
        print("Todas as bolas foram sorteadas.")
        break

#print(jogo)
print(f"Todas as bolas sorteadas (método): {jogo.todas_sorteadas()}")
