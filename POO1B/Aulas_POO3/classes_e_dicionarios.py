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

arquivo = open("clientes.json", mode="w")
json.dump(clientes, arquivo, default = vars)
arquivo.close()
#2 tipos de abordagem que cria, faz o dump e fecha o arquivo
# com o with, o arquivo é fechado automaticamente
#with open("clientes.json", mode="w") as arquivo:
#    json.dump(clientes, arquivo, default = vars)




print(x)
print(x.__dict__)
print(vars(x))
print()
print(y)
print(y.__dict__)