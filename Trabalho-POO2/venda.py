import json

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