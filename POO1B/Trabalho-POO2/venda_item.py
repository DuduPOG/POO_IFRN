import json

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
        with open("venda_itens.json", mode="r") as arquivo:
            s = json.load(arquivo)
            for dic in s: 
                c = VendaItem(dic["id"], dic["qtd"], dic["preco"])
                c.id_venda = dic["id_venda"]
                c.id_produto = dic["id_produto"]
                cls.objetos.append(c)


    @classmethod
    def salvar(cls):
        with open("venda_itens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)