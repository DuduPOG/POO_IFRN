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