import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f'{self.id} - {self.nome}'
    
x = Cliente("1", "Joao")
y = Cliente("2", "Maria")

clientes = [x, y]

lista = []
with open("clientes.json", mode="r") as arquivo:
    clientes_json = json.load(arquivo)
    for dic in clientes_json:
        #print(disc)
        c = Cliente(dic["id"], dic["nome"])
        lista.append(c)
        print(dic, c)
        