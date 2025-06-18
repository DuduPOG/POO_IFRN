#import datetime
from datetime import datetime, timedelta
import pytz

# módulo/arquivo.classe
#x = datetime.datetime(2025, 5, 12, 16, 49)

# classe
x = datetime(2025, 5, 12)
print(x)

y = datetime(2025, 5, 12, 16, 51)
print(y)

z = datetime(2024, 2, 29, 17, 0, 20)
print(z)

print()

#agora
a = datetime.now(pytz.timezone('America/Sao_Paulo'))
b = datetime.today()
print(a)
print(b)
print()

#p = input("Informe sua data no formato dd/mm/YYYY\n")
p = "12/05/2025, 16:30"
#p = input("Informe sua data e hora de nascimento no formato dd/mm/YYYY, %H:%M\n")
c = datetime.strptime(p, "%d/%m/%Y, %H:%M")
print(p)
print()
print(c)

print(c.day, c.month, c.year)

print(c.date())

print(c.time())

print(c.weekday())

print(c.strftime("%d/%m/%Y"))

print(c.strftime("%d/%m/%Y, %H:%M"))

print(c.strftime("%A, %d/%B/%Y"))

x = timedelta(hours=1, minutes=30)
print(x) #timedelta
print(c) #datetime
print(x + c) #timedelta + datetime = datetime

hoje = datetime.today()
print(hoje + x)