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
        self.__limite = limite
        self.__socio = None


    def set_nome(self, nome):
        self.__nome=nome

    def get_nome(self):
        return self.__nome
    
    def set_limite(self, limite):
        self.__nome=limite

    def get_limite(self):
        return self.__limite
    
    # MEXER AQUI
    def set_socio(self, cliente): #69 c1.set_socio(c2)
        self.__socio=cliente      # c1.__socio = c2
        cliente.__socio = self    # c2.__socio = c1

    def get_socio(self):
        return self.__socio

    def __str__(self):
        if self.__socio == None:
            return f"{self.__nome}, seu limite é de R$ {self.__limite}"
        else:
            s = f"{self.__nome}, seu limite é de R$ {self.__limite:.2f}"
            s += f", seu sócio é {self.__socio.__nome}"
            return s 

    pass

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
        return int(input("Selecione uma ação: 1-Criar Playlist, 2-Inserir música, 3-Listar músicas, 10-Fim\n"))
    
    @staticmethod
    def main():
        op=0
        x = None
        while op!=10:
            op=UI.menu()
            if op==1:  
                x=UI.criar_playlist()
            elif op==2:
                if x==None:
                    print("Crie uma playlist antes de inserir as músicas!")
                UI.inserir_musica(x)
            elif op==3:
                if x==None:
                    print("Crie uma playlist antes de listar as músicas!")
                UI.listar_musicas(x)

    @staticmethod
    def criar_playlist():
        nome = input("Informe o nome da playlist: ")
        descricao = input("Informe uma descrição: ")
        x=PlayList(nome, descricao)
        return x
    
    @staticmethod
    def inserir_musica(x):
        titulo = input("Informe o título da música: ")
        artista = input("Informe o artista/banda da música: ")
        album = input("Informe o álbum: ")
        musica = Musica(titulo, artista, album)
        x.inserir(musica)

    @staticmethod
    def listar_musicas(x):
        for musica in x.listar():
            print(" ", musica)

UI.main()
"""