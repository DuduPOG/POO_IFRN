from datetime import datetime, timedelta

class Carrinho:
    def __init__(self):
        self.__cliente = ""
        self.__data = datetime.today()
        self.__itens = []


    def set_cliente(self, v):
        if v == "":
            raise ValueError("O cliente deve ter um nome válido!")
        else:
            self.__cliente = v

    def set_data(self, v):
        if v > datetime.today():
            raise ValueError("A data não pode ser no futuro!")
        else:
            self.__data = v

    def get_cliente(self):
        return self.__cliente

    def get_data(self):
        return self.__data
    
    def inserir_item(self, v):
      self.__itens.append(v)

    def remover_item(self, v):
        if self.__itens == []:
            raise ValueError("Não é possível remover itens de um carrinho vazio")
        elif v not in self.__itens:
            raise ValueError("Não é possível remover um item que não está no carrinho")
        else:
            self.__itens.remove(v)

    def listar_itens(self):
        return self.__itens
    
    def custo_total(self):
        total = 0
        for item in self.__itens:
            total += item.custo_total()
        return total
    
    def __str__(self):
        return f"Este carrinho é do/da cliente {self.__cliente}, organizado na data: {self.__data}, com {len(self.__itens)} item(ns)"
    
    
    pass


class Item:
    def __init__(self):
        self.__produto = ""
        self.__qtd = 0
        self.__preco = 0

    def set_produto(self, v):
        if v == "":
            raise ValueError("O produto deve ter um nome válido!")
        else:
            self.__produto = v

    def set_qtd(self, v):
        if v <= 0:
            raise ValueError("Quantidade inválida!")
        else:
            self.__qtd = v

    def set_preco(self, v):
        if v <= 0:
            raise ValueError("Não existe almoço grátis!")
        else:
            self.__preco = v

    def get_produto(self):
        return self.__produto
    
    def get_qtd(self):
        return self.__qtd
    
    def get_preco(self):
        return self.__preco
    
    def custo_total(self):
        return self.__qtd * self.__preco

    def __str__(self):
        s = f"Este é produto {self.__produto}, tem um preço unitário de: R$ {self.__preco:.2f},"
        s += f" foi/foram adicionada(s) {self.__qtd} unidade(s), custando no total: R$ {self.custo_total():.2f}\n" 
        return s

    pass

x = Carrinho()
x.set_cliente("João")
x.set_data(datetime(2025, 5, 12, 16, 49))

y = Item()
y.set_produto("Arroz")
y.set_qtd(2)
y.set_preco(5)
x.inserir_item(y)

z = Item()
z.set_produto("Feijão")
z.set_qtd(1)
z.set_preco(10)
x.inserir_item(z)

a = Item()
a.set_produto("Carne")
a.set_qtd(1)
a.set_preco(20)
x.inserir_item(a)

x.remover_item(z)


print(x)
print()
print(f"Este foi o custo total do carrinho de compras: R${x.custo_total():.2f}")
print()
print("Itens do carrinho:")
for itens in x.listar_itens():
    print(itens)