from datetime import datetime, timedelta
"""
import json

# tipo de dado inválido
x = int(input("Informe um número: "))
print(x)

# estouro de pilha (falha na recursão)
def func(x):
    print(x)
    func(x + 1)
print(func(x))

# lançamento de exceção
x = int(input("Informe um número: "))
if x < 10:
    raise ValueError("Lançando um erro!")

try:
    n = int(input("Informe um número inteiro: "))
    print(2 * n)
except:
    print("Você não digitou um número inteiro!")

#erro de arquivo
with open("categorias2.json", mode="r") as arquivo:
    s = json.load(arquivo)

#erro de índice
x = [1, 2, 3]
print(x[10])

#erro de chave
x = {"A" : "Abacaxi", "B" : "Banana", "C" : "Caju"}
print(x["D"])

#erro de valor
try:
    a = int(input("Informe o dividendo: "))
    b = int(input("Informe o divisor: "))
    print(a/b)
except Exception as erro:
    print(type(erro))
    print(erro)

#erros específicos
try:
    a = int(input("Informe o dividendo: "))
    b = int(input("Informe o divisor: "))
    print(a/b)
except ValueError:
    print("Informe números inteiros")
except ZeroDivisionError:
    print("Informe um divisor não nulo")

#erro específico e um outro trecho de código que sempre será executado por completo (finally)
try:
    a = int(input("Informe o dividendo: "))
    b = int(input("Informe o divisor: "))
    print(a/b)
except ValueError as erro:
    print(erro)
finally:
    print("Ok")
print("Fim")

"""
# laço para o programa não encerrar enquanto der erro de valor na data
erro = True
while erro:
    s = input("Informe uma data no seguinte formato dd/mm/aaaa: ")
    try:
        d = datetime.strptime(s, "%d/%m/%Y")
        t = timedelta(days = 1)
        d += t
        print(d)
        erro = False
    except:
        print("Você não digitou uma data válida!") 