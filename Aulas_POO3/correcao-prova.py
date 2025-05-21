from datetime import datetime


class Cliente:

    def __init__(self):
        #self.__id = None
        self.__nome = None
        self.__data_cadastro = None
        #a lista poderia ser eliminada, pois cada cliente teria um id
        self.__contratos = []


    def set_nome(self, nome):
        if nome == "":
            raise ValueError("O nome não pode ficar vazio!")
        else:
            self.__nome = nome


    def get_nome(self):
        return self.__nome


    def set_data_cadastro(self, data_cadastro):
        if data_cadastro > datetime.now():
            raise ValueError("A data de cadastro não pode ser futura!")
        elif data_cadastro == "":
            raise ValueError("A data de cadastro não pode ficar vazia!")
        else:
            self.__data_cadastro = data_cadastro


    def get_data_cadastro(self):
        return self.__data_cadastro
    
    
    def inserir(self, c):
        if c in self.__contratos:
            raise ValueError("Este contrato já existe!")
        else:
           self.__contratos.append(c)


    def remover(self, c):
        if c not in self.__contratos:
            raise ValueError("Este contrato não existe!")
        else:
            self.__contratos.remove(c)


    def listar(self):
        return self.__contratos
    
   
    def tempo_cadastro(self):
        t = datetime.now() - self.__data_cadastro #timedelta
        anos = t.days // 365
        dias = anos % 365
        meses = dias // 30
        return f"{anos} ano(s) e {meses} mês/meses"


    def total(self):
        t = 0
        for c in self.__contratos:
            t += c.get_valor()
        return t
    

    def __str__(self):
        return f"O cliente {self.__nome}, registrado em: {self.__data_cadastro.strftime("%d/%m/%Y")}, tem {len(self.__contratos)} contrato(s)"


    pass


class Contrato:

    def __init__(self, plano, ddd, numero, valor):
        #self.__id = None
        self.__plano = plano
        self.__ddd = ddd
        self.__numero = numero
        self.__valor = valor
        #self.__cliente = None


    def set_plano(self, plano):
        if plano == "":
            raise ValueError("O plano não pode ficar vazio!")
        else:
            self.__plano = plano
    

    def get_plano(self):
        return self.__plano
    

    def set_ddd(self, ddd):
        if ddd < 0 or ddd > 99:
            raise ValueError("O DDD deve ser um número entre 0 e 99!")
        else:
            self.__ddd = ddd


    def get_ddd(self):
        return self.__ddd


    def set_numero(self, numero):
        if numero < 0 or numero > 99999999:
            raise ValueError("O número deve ser um número entre 0 e 99999999!")
        else:
            self.__numero = numero


    def get_numero(self):
        return self.__numero
    

    def set_valor(self, valor):
        if valor < 0:
            raise ValueError("O valor não pode ser negativo!")
        else:
            self.__valor = valor


    def get_valor(self):
        return self.__valor
    

    def __str__(self):
        return f"Este é o plano {self.__plano}, contato do contratante: ({self.__ddd}) {self.__numero}, valor do contrato: R$ {self.__valor:.2f}"

    pass    


x = Cliente()
x.set_nome("João")
x.set_data_cadastro(datetime.strptime("01/01/2024", "%d/%m/%Y"))

y = Contrato("Plano Básico", 84, 99999999, 10.10)#, c
z = Contrato("Plano Premium", 84, 999999999, 50.50)#, c
a = Contrato("Plano Avançado", 84, 99999999, 100.10)#, c

#com cada cliente tendo um id, eliminaria a necessidade de criar uma lista de contratos
# e poderia usar o id para buscar o cliente na lista de clientes
# e o id do cliente para buscar o contrato na lista de contratos

x.inserir(y)
x.inserir(z)
x.inserir(a)

print(x)
print()

for c in x.listar():
    print(c)
    print(f"É cliente há: {x.tempo_cadastro()}\n")

print(f"Esta é a soma mensal dos contratos: R$ {x.total():.2f}")