from datetime import datetime, timedelta


class Atleta:

    def __init__(self):
        self.__nome=""
        self.__nascimento=datetime.today()
        self.__treinos = []


    def inserir_treinos(self, v):
        self.__treinos.append(v)

    
    def remover_treinos(self, v):
        self.__treinos.remove(v)


    def listar_treinos(self):
        return self.__treinos


    def set_nome(self, v):

        if v == "":
            raise ValueError("É necessário um nome válido!")
        else:
            self.__nome = v


    def set_nascimento(self, v):
        if v > datetime.today():
            raise ValueError("Você não pode nascer no futuro!")
        else:
            self.__nascimento = v


    def get_nome(self):
        return self.__nome
    
    
    def get_nascimento(self):
        return self.__nascimento
    

    def distancia_total(self):
        total = 0
        for treino in self.__treinos:
            total += treino.get_distancia()
        return total
    

    def menor_pace(self):
        p = []
        for treino in self.__treinos:
            p.append(treino.pace())
        return min(p)


    def __str__(self):
        return f"{self.__nome} é um atleta que nasceu em: {self.__nascimento.strftime("%d/%m/%Y")} e já treinou {len(self.__treinos)} vez(es)\n"
    pass


        
class Treino:

    def __init__(self):
        self.__data_treino=datetime.today()
        self.__distancia=0 #em metros
        self.__tempo=timedelta(hours=0, minutes=0, seconds=0) #transformar a data em segundos e trasnformar em minutos


    def set_data_treino(self, v):
        self.__data_treino = v


    def set_distancia(self, v):
        if v <= 0:
            raise ValueError("Insira uma distância válida!")
        else:
            self.__distancia = v

    
    def set_tempo(self, v):
        if v > datetime.today():
            raise ValueError("Insira um tempo válido!")
        else:
            self.__tempo = v


    def get_data_treino(self):
        return self.__data_treino
    
    
    def get_distancia(self):
        return self.__distancia


    def pace(self):

        if self.__distancia <= 0:
            raise ValueError("A distância não pode ser menor ou igual a zero!")

        else:
            # converte a distancia para km
            self.__distancia = self.__distancia / 1000
            
            # converte o tempo para minutos
            self.__segundos = self.__tempo.total_seconds()
            self.__minutos = self.__segundos / 60

            # calcula o pace em minutos por km
        return self.__minutos / self.__distancia
    
    
    def __str__(self):
        to_string = f"Este treino foi realizado na data: {self.__data_treino.strftime("%d/%m/%Y %H:%M")} com a distância percorrida de {self.__distancia} metros neste tempo: {self.__tempo};\n"
        to_string += f"resultando em {self.pace():.2f} de pace\n"
        return to_string
    pass


#digitar a data de nascimento como: dd/mm/YYYY, "%d/%m/%Y"

x = Atleta()
x.inserir_treinos(1)
x.set_nome("Lucas")
x.set_nascimento(datetime.strptime("10/06/2005", "%d/%m/%Y"))
print(x)
print("Treinos do atleta")
for treino in x.listar_treinos():
    print(treino)
    print("Pace =", x.menor_pace())

y = Treino()
y.set_data_treino(datetime.strptime("10/06/2023", "%d/%m/%Y"))
y.set_distancia(5000)
y.set_tempo(timedelta(hours=0, minutes=40, seconds=10))
print(y)