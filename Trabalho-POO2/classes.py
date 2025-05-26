from datetime import datetime

class Categoria:

    def __init__(self, id, desc):
        self.id = id
        self.desc = desc


    def __str__(self):
        return f"{self.id} - {self.desc}"
    

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone


    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"


class Venda:
    def __init__(self, id, data, carrinho, total, id_cliente):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.id_cliente = id_cliente


class VendaItem:
    def __init__(self, id, qtd, preco, id_venda, id_produto):
        self.id = id
        self.qtd = qtd
        self.preco = preco
        self.id_venda = id_venda
        self.id_produto = id_produto


class Produto:
    def __init__(self, id, desc, preco, estoque, id_categoria):
        self.id = id
        self.desc = desc
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = id_categoria