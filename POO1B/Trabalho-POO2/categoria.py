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
            with open("categorias.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    c = Categoria(dic["id"], dic["desc"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass


    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)