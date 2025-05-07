class PlayList:
    def __init__(self, nome, descricao):
        self.__nome=nome
        self.__descricao=descricao
        self.__musicas=[]

    def inserir(self,m):
        self.__musicas.append(m)

    def listar(self):
        return self.__musicas    
        

    def __str__(self):
        return f"Playlist {self.__nome} tem {len(self.__musicas)} músicas"

    pass

class Musica:
    def __init__(self, titulo, artista, album):
        self.__titulo=titulo
        self.__artista=artista
        self.__album=album


    def __str__(self):
        return f"{self.__titulo} - {self.__artista} - {self.__album}"
    
    pass

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
x=PlayList("Rock", "Minhas músicas de rock preferidas")
y=PlayList("Axé", "Show Ivete Sangalo - Maracanã")

m1=Musica("Hotel California","Eagles","Eagles")
m2=Musica("Bete Balanço", "Barão Vermelho", "Grandes Músicas anos 80")
m3=Musica("Arerê", "Ivete Sangalo", "Show Maracanã")

x.inserir(m1)
x.inserir(m2)
y.inserir(m3)

print(x)
for musica in x.listar():
    print(" ",musica)

print(y)
for musica in y.listar():
    print(" ",musica)
"""