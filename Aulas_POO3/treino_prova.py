from datetime import datetime, timedelta

class Atleta:
    def __init__(self):
        self.__nome=""
        self.__nascimento=datetime.today()

    def set_nome(self, v):
        if v == "":
            raise ValueError("É necessário um nome válido!")
        else:
            self.__nome = v

    def set_nascimento(self, v):
        self.__nascimento = v

    def get_nome(self):
        return self.__nome
    
    def get_nascimento(self):
        return self.__nascimento

    def __str__(self):
        return f"{self.__nome} é um atleta que nasceu em: {self.__nascimento.strftime("%d/%m/%Y")}\n"
    pass
        
class Treino:
    def __init__(self):
        self.__data_treino=datetime.today()
        self.__distancia=0 #em metros
        self.__tempo=timedelta(hours=0, minutes=0, seconds=0) #transformar as horas em minutos e somar com os minutos já registrados

    def set_data_treino(self, v):
        self.__data_treino = v

    def set_distancia(self, v):
        if v <= 0:
            raise ValueError("Insira uma distância válida!")
        else:
            self.__distancia = v
    
    def set_tempo(self, v):
        if v == self.__tempo:
            raise ValueError("Insira um tempo válido!")
        else:
            self.__tempo = v

    def get_data_treino(self):
        return self.__data_treino
    
    def get_distancia(self):
        return self.__distancia

    def pace(self):
        if self.__distancia == 0:
            raise ValueError("A distância não pode ser zero!")
        else:
            # pace = tempo / distancia
            # tempo = timedelta
            # distancia = float
            # pace = timedelta / float
            # pace = timedelta
            # converte a distancia para km
            self.__distancia = self.__distancia / 1000
            # converte o tempo para minutos
            # self.__tempo = timedelta(hours=self.__tempo.hour, minutes=self.__tempo.minute, seconds=self.__tempo.second)
            #horas = self.__tempo.minutes // 60
            #segundos = self.__tempo.seconds % 60
            #self.__tempo = self.__tempo.total_minutes()
            # calcula o pace em minutos por km
        return self.__tempo/self.__distancia
    
    def __str__(self):
        to_string = f"Este treino foi realizado na data: {self.__data_treino} com a distância percorrida de {self.__distancia} e tempo de {self.__tempo},\n "
        to_string += f"resultando em {self.pace()} de pace\n"
        return to_string
    pass

#digitar a data de nascimento como: dd/mm/YYYY, "%d/%m/%Y"

x = Atleta()
x.set_nome("Lucas")
x.set_nascimento(datetime.strptime("10/06/2005", "%d/%m/%Y"))
print(x)

y = Treino()
y.set_data_treino(datetime.strptime("10/06/2023", "%d/%m/%Y"))
y.set_distancia(10000)
y.set_tempo(timedelta(hours=1, minutes=10, seconds=20))
print(y)