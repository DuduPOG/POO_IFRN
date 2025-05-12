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
        if v == datetime.today:
            raise ValueError("Insira uma data válida!")
        else:
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
        self.__distancia=0 #em km
        self.__tempo=timedelta(hours=0, minutes=0) #transformas as horas em minutos e somar com os minutos já registrados

    def set_data_treino(self, v):
        if v == datetime.today():
            raise ValueError("É necessário uma data válida!")
        else:
            self.__nome = v

    def set_distancia(self, v):
        if v <= 0:
            raise ValueError("Insira uma distância válida!")
        else:
            self.__distancia = v

    def get_data_treino(self):
        return self.__data_treino
    
    def get_distancia(self):
        return self.__distancia

    def pace(self):
        return self.__tempo/self.__distancia
    
    def __str__(self):
        to_string = f"Este treino foi realizado na data: {self.__data_treino} com a distância percorrida de {self.__distancia} e tempo de {self.__tempo},\n "
        to_string += f"resultando em {self.pace():.2f} de pace\n"
        return to_string
    pass

#digitar a data de nascimento como: dd/mm/YYYY, "%d/%m/%Y"