from datetime import datetime, timedelta

class Carrinho:
    def __init__(self):
        self.__cliente = None
        self.__data = datetime.today()
        self.__itens = []
    
    def inserir_item(self, v):
        if v == 0:
            raise ValueError("Não é possível adicionar 0 itens no carrinho")
        else:
            self.__itens.append(v)

    def remover_item(self, v):
        if self.__itens == []:
            raise ValueError("Não é possível remover itens de um carrinho vazio")
        elif v is not self.__itens:
            raise ValueError("Não é possível remover um item que não está no carrinho")
        else:
            self.__itens.remove(v)

    def listar_itens(self):
        return self.__itens
    
    def custo_total(self):
        return self.__itens
    
    def __str__(self):
        return f"Este carrinho é do/da cliente {self.__cliente}, organizado na data: {self.__data}, com {len(self.__itens)} item(ns)"
    
    
    pass


class Item:
    def __init__(self):
        self.__produto = None
        self.__qtd = 0
        self.__preco = 0

    def get_produto(self, v):
        if v == "":
            raise ValueError("O produto deve ter um nome válido!")
        else:
            self.__produto = v

    def get_qtd(self, v):
        if v <= 0:
            raise ValueError("Quantidade inválida!")
        else:
            self.__qtd = v

    def get_preco(self, v):
        if v <= 0:
            raise ValueError("Não existe almoço grátis!")
        else:
            self.__preco = v

    def __str__(self):
        return f""



    pass