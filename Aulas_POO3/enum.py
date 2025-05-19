"""
class Estacao(enum.Enum):
    OUTONO = 1
    INVERNO = 2
    PRIMAVERA = 3
    VERÃO = 4
    pass

a = Estacao.Outono
b = Estacao["INVERNO"]
c = Estacao(3)

print(a)
print(b)
print(c)

class EstadoCivil(enum.Enum):
    Solteiro = 1
    Casado = 2
    Divorciado = 3
    Viúvo = 4
    

class Pessoa:
    def __init__(self):
        self.nome = ""
        self.estado_civil = EstadoCivil.Solteiro

    def __str__(self):
        return f"{self.nome} é {self.estado_civil}"

x = Pessoa()
print()
print(x.nome)
print(x.estado_civil)
print()
print(x)
"""
import enum

class Dia(enum.IntFlag):
    Domingo = 1
    Segunda = 2
    Terca = 4
    Quarta = 8
    Quinta = 16
    Sexta = 32
    Sabado = 64

x = Dia.Domingo
print(x.value, x.name)

y = Dia(0)
print(y.value, y.name)

z = Dia.Sabado | Dia.Domingo
print(z.value, z.name)