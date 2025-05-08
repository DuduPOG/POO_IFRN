class Empresa:
    def __init__(self, nome):
        if nome == " ":
            raise ValueError("Empresa não pode ficar sem nome!")
        self.__nome = nome
        self.__clientes =[] # 1 ---> * Uma empresa pode ter vários clientes

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def inserir(self, cliente):
        self.__clientes.append(cliente)

    def listar(self):
        return self.__clientes

    def __str__(self):
        return f"{self.__nome} tem {len(self.__clientes)} cliente(s)"

    pass

class Cliente:
    def __init__(self, nome, limite):
        if nome == " " or limite < 0:
            raise ValueError("O cliente não pode ficar sem nome nem com limite negativo!")
        self.__nome = nome
        self.__limite = float(limite)
        self.__socio = None

    def set_nome(self, nome):
        self.__nome=nome

    def get_nome(self):
        return self.__nome
    
    def set_limite(self, limite):
        self.__nome=limite

    def get_limite(self):
        if self.__socio != None:
            return self.__limite + self.__socio.__limite
        return self.__limite
    
    def set_socio(self, cliente): #69 c1.set_socio(c2)
        if self.__socio != None:
            self.__socio.__socio = None #socio atual

        if cliente.__socio != None:
            cliente.__socio.__socio = None

        self.__socio=cliente      # c1.__socio = c2
        cliente.__socio = self    # c2.__socio = c1

    def get_socio(self):
        return self.__socio
    
    def __str__(self):
        if self.__socio == None:
            return f"{self.__nome}, seu limite é de R$ {self.__limite}"
        else:
            s = f"{self.__nome}, seu limite é de R$ {self.get_limite():.2f}"
            s += f", seu/sua sócio(a) é {self.__socio.__nome}"
            return s 
    pass

"""
x=Empresa("IFRN")
print(x)

print()

c1 = Cliente("Eduardo", 1000)
c2 = Cliente("Lucas", 2000)
c3 = Cliente("Júlia", 1500)
c4 = Cliente("Daniele", 2500)

c1.set_socio(c2) # self -> c1 | cliente cliente -> c2
#c2.set_socio(c1)
c4.set_socio(c3)

x.inserir(c1)
x.inserir(c2)
x.inserir(c3)
x.inserir(c4)

print(x)
print()
for clientes in x.listar():
    print(" ", clientes)

print()
c1.set_socio(c3)
for clientes in x.listar():
    print(" ", clientes)

"""
    
class UI:

    @staticmethod
    def menu():
        return int(input("Selecione uma ação: 1-Criar uma empresa, 2-Inserir um cliente na empresa, 3-Criar uma sociedade entre clientes, 10-Fim\n"))
    
    @staticmethod
    def main():
        op=0
        x = None
        y = 0
        while op!=10:
            op=UI.menu()
            if op==1:
                x=UI.criar_empresa()
            elif op==2:
                if x==None:
                    print("Crie uma empresa antes de inserir os clientes na empresa!")
                UI.inserir_cliente(x)
                y+=1
            elif op==3:
                if x==None and y < 2:
                    print("Crie uma empresa e tenha pelo menos 2 clientes por empresa antes de criar uma sociedade!")
                UI.criar_sociedade(x)

    @staticmethod
    def criar_empresa():
        nome = input("Informe o nome da empresa: ")
        x=Empresa(nome)
        return x
    
    @staticmethod
    def inserir_cliente(x):
        nome = input("Informe o nome do cliente: ")
        limite = float(input("Informe o limite de crédito do cliente: "))
        y=Cliente(nome, limite)
        x.inserir(nome)

    @staticmethod
    def criar_sociedade(x):
        n = 0
        clientes = x.listar()
        for cliente in clientes:
            print(n, "-", cliente)
            n += 1
        a = int(input("Informe o número do 1º cliente: "))
        b = int(input("Informe o número do 2º cliente: "))
        clientes[a].set_socio(clientes[b])
        print(x)

UI.main()
