x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"} #chaves podem ser strings, números ou tuplas
y = [1, 2, 3, 4]
del y[3]
z = (1, 2, 3, 4)

x["AM"] = "Manaus"
x["RJ"] = "Rio de Janeiro"

print(x)
print(type(x), type(y), type(z))
print()
print(x["PE"], y[2], z[1])
print(len(x), len(y), len(z))
print()

x[5] = y
print()

x["Nordeste"] = "Natal", "João Pessoa", "Recife"
del x["RN"] #ou x.pop("RN")
print(x)
print(*x)
print(x["Nordeste"])
print()

for item in x.items():
    print(item)
print()

for chave in x.keys():
    print(chave)
