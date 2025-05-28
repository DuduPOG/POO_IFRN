"""
from datetime import datetime
import json

class Categoria:

    def __init__(self, id, desc):
        self.id = id
        self.desc = desc


    def __str__(self):
        return f"{self.id} - {self.desc}"
    

class Categorias:

    objetos = []


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        maior = 0
        for id in cls.objetos:
            if id.id > maior:
                maior = id.id
            id.id = maior + 1
        cls.objetos.append(obj)
        cls.salvar() 


    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None
    

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("comercio_eletronico.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    c = Categoria(dic["id"], dic["desc"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass


    @classmethod
    def salvar(cls):
        with open("comercio_eletronico.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    

class Cliente:

    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone


    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"


class Clientes:

    objetos = []


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        maior = 0
        for id in cls.objetos:
            if id.id > maior:
                maior = id.id
            id.id = maior + 1
        cls.objetos.append(obj)
        cls.salvar() 


    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None
    

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:    
            with open("comercio_eletronico.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    c = Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass


    @classmethod
    def salvar(cls):
        with open("comercio_eletronico.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
        


class Venda:

    def __init__(self, id, data, carrinho, total):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.id_cliente = 0


    def __str__(self):
        return f"{self.id} - {self.data} - {self.carrinho} - {self.total} - {self.id_cliente}"
    

class Vendas:

    objetos = []


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        maior = 0
        for id in cls.objetos:
            if id.id > maior:
                maior = id.id
            id.id = maior + 1
        cls.objetos.append(obj)
        cls.salvar() 


    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None
    

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    
    
    @classmethod
    def abrir(cls):
        cls.objetos = []    
        with open("comercio_eletronico.json", mode="r") as arquivo:
            s = json.load(arquivo)
            for dic in s: 
                c = Venda(dic["id"], dic["data"], dic["carrinho"], dic["total"], dic["id_cliente"])
                cls.objetos.append(c)


    @classmethod
    def salvar(cls):
        with open("comercio_eletronico.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)


class VendaItem:

    def __init__(self, id, qtd, preco):
        self.id = id
        self.qtd = qtd
        self.preco = preco
        self.id_venda = 0
        self.id_produto = 0


    def __str__(self):
        return f"{self.id} - {self.qtd} - {self.preco} - {self.id_venda} - {self.id_produto}"
    

class VendaItens:

    objetos = []


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        maior = 0
        for id in cls.objetos:
            if id.id > maior:
                maior = id.id
            id.id = maior + 1
        cls.objetos.append(obj)
        cls.salvar() 


    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None
    

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    
    
    @classmethod
    def abrir(cls):
        cls.objetos = []    
        with open("comercio_eletronico.json", mode="r") as arquivo:
            s = json.load(arquivo)
            for dic in s: 
                c = VendaItem(dic["id"], dic["qtd"], dic["preco"], dic["id_venda"], dic["id_produto"])
                cls.objetos.append(c)


    @classmethod
    def salvar(cls):
        with open("comercio_eletronico.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)



class Produto:

    def __init__(self, id, desc, preco, estoque):
        self.id = id
        self.desc = desc
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = 0


    def __str__(self):
        return f"{self.id} - {self.desc} - {self.preco} - {self.estoque} - {self.id_categoria}"
    

class Produtos:

    objetos = []


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        maior = 0
        for id in cls.objetos:
            if id.id > maior:
                maior = id.id
            id.id = maior + 1
        cls.objetos.append(obj)
        cls.salvar() 


    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None
    

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:  
            with open("comercio_eletronico.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    c = Produto(dic["id"], dic["desc"], dic["preco"], dic["estoque"])
                    c.id_categoria = dic["id_categoria"]
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass


    @classmethod
    def salvar(cls):
        with open("comercio_eletronico.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

"""