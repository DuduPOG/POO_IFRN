import json

class Produto:

    def __init__(self, id, desc, preco, estoque, id_categoria):
        self.id = id
        self.desc = desc
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = id_categoria


    def __str__(self):
        return f"{self.id} - {self.desc} - {self.preco} - {self.estoque} - {self.id_categoria}"
    

class Produtos:

    objetos = []


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        if cls.objetos:
            maior = max(cliente.id for cliente in cls.objetos)
            obj.id = maior + 1
        else:
            obj.id = 0
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
            with open("produtos.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    c = Produto(dic["id"], dic["desc"], dic["preco"], dic["estoque"], dic["id_categoria"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass


    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)