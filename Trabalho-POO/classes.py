import json


class Cliente:

    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone


    def set_id(self, id):
        if id > 0:
            self.__id = id
        else:
            raise ValueError("ID deve ser maior que 0")
        
        
    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            raise ValueError("Nome não deve ser vazio")
        

    def set_email(self, email):
        if email != "":
            self.__email = email
        else:
            raise ValueError("Email não deve ser vazio")
        

    def set_fone(self, fone):
        if fone != "":
            self.__fone = fone
        else:
            raise ValueError("Telefone não deve ser vazio")
        
        
    def get_id(self):
        return self.__id
    

    def get_nome(self):
        return self.__nome
    

    def get_email(self):
        return self.__email
    

    def get_fone(self):
        return self.__fone
    

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}\n"
    
    pass

    
class Clientes:
    objetos = [] #atributo de classe/estático

    @classmethod
    def inserir(cls, c):
        cls.abrir()
        cls.objetos.append(c)
        cls.salvar()

    @classmethod
    def excluir(cls, id):
        for id in Clientes.objetos:
            if cls.objetos[id].get_id() == id:
                del (cls.objetos[id])
                break
        else:
            raise ValueError("ID não encontrado")
    
    """
    @classmethod
    def atualizar(cls, id, nome, email, fone):
        for i in range(len(self.__clientes)):
            if self.__clientes[i].get_id() == id:
                self.__clientes[i].set_nome(nome)
                self.__clientes[i].set_email(email)
                self.__clientes[i].set_fone(fone)
                break
        else:
            raise ValueError("ID não encontrado")
    """
    
    @classmethod
    def listar(cls):
        return cls.objetos
    
    @classmethod
    def salvar(cls):
        arquivo = open("clientes.json", mode="w")
        with open("clientes.json", "w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        lista = []
        with open("clientes.json", mode="r") as arquivo:
            clientes_json = json.load(arquivo)
            for dic in clientes_json:
                c = Cliente(dic["id"], dic["nome"])
                lista.append(c)
                print(dic, c)

    pass
        