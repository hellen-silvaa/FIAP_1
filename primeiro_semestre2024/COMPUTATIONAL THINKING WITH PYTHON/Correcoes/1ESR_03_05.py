'''comprimento = 0
for char in 'danilo':
    comprimento += 1
print(comprimento)

for i in range(10):#start, end, step
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(10,1,-2):
    print(i)

for i in range(10):
    print(i,end = ' ')
    i = 1
    print(i)

pares = 0
for i in range(1,11):
    num = input("Diga um numero: ")
    while not num.isnumeric():
        num = input("Diga um numero: ")
    num = int(num)
    if num % 2 == 0:
        pares += 1
print(f"Vc digitou {pares} pares e {i - pares} impares")

soma = 0
for i in range(1,11):
    num = input("Diga um numero: ")
    while not num.isnumeric():
        num = input("Diga um numero: ")
    num = int(num)
    soma += num
print(f"A soma é {soma} e a média é {soma/i}")

soma = 0
for i in range(1,101):
    soma += i
print(soma)


i = 1
while i <= 10:
    print(f"Tabuada do {i}:")
    j = 1
    while j <= 10:
        print(f"{i} * {j} = {i*j}")
        j += 1
    i += 1
    print()

for i in range(1,11):
    print(f"Tabuada do {i}:")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()

vogais = 0
nome = 'danilo'
for char in nome:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o'\
            or char == 'u':
        vogais += 1
print(f"Há {vogais} vogais e {len(nome) - vogais}"
      f" consoantes em {nome}")


a = 1
b = a
b = 2
print(a)

a = [1,2,3]
b = a
b[0] = 5
print(a)
a = [43,3,46,2]
print(a)
print(b)



lista = [6,True,'sdhgiofhd',[],4.2]

for i in range(len(lista)):
#    print(f"lista[{i}] = {lista[i]}")
    lista[i] = 1
print(lista)
for elem in lista:
    elem = 1
print(lista)

num = input('diga uma coisa: ')
lista = []
lista.append(num)
print(lista)
lista.append(111)
print(lista)
lista.append(11)
print(lista)
'''
#1 - Declare uma lista com 10 numeros. Faça a soma e a media dos
#numeros loopando nela.
lista = [4,3,1,0,2,3,10,1,11,98]
soma = 0
for num in lista:
    soma += num
print(soma,soma/len(lista))

soma = 0
for i in range(len(lista)):
    soma += lista[i]
print(soma,soma/len(lista))
#2 - Declare uma lista com 10 numeros. Coloque os pares em uma
# nova lista e os impares tambem.
lista = [4,3,1,0,2,3,10,1,11,98]
pares = []
impares = []
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
        continue
    impares.append(lista[i])
    print(pares)
    print(impares)


















