'''
#Exercício 1
primeiro_numero = int(input("Diga o primeiro número: "))
segundo_numero = int(input("Diga o segundo número: "))
if primeiro_numero > segundo_numero:
    print(primeiro_numero)
else:
    print(segundo_numero)
#Exercício 2
ano = int(input("Diga seu ano de nascimento: "))
idade = 2024 - ano
if idade >= 18:
    print("É obrigatório votar")
elif idade >= 16:
    print("É opcional votar")
else:
    print("Não pode votar")
#Exercício 3
senha = int(input("Diga sua senha: "))
senha_cadastrada = 1234
print(type(senha_cadastrada))
if senha == senha_cadastrada:
    print("Acesso Liberado")
else:
    print("Acesso Negado")

senha = input("Diga sua senha: ")
senha_cadastrada = '1234'
if senha == senha_cadastrada:
    print("Acesso Liberado")
else:
    print("Acesso Negado")
#Exercício 4
qtd = int(input("Qts maçãs? "))
preco = 0.3
if qtd >= 12:
    preco = 0.25
print(f"Você pagará R${qtd*preco:.2f}")
#Exercício 6
sx = int(input("Digite o número correspondente: 1-feminino, 2-masculino"))
altura = float(input("Diga sua altura: "))
peso = 72.7*altura - 58
if sx == 1:
    peso = 62.1*altura - 44.7
print(f"Seu peso ideal é {peso}kg")
#Exercício 7
lados = int(input("Diga o número de lados: "))
valor = int(input("Diga o tamanho do lado: "))
if lados == 3:
    forma = 'triângulo'
    perimetro = 3*valor
elif lados == 4:
    forma = 'quadrado'
    perimetro = 4*valor
else:
    forma = 'pentágono'
    perimetro = 5*valor
print(f"Você escolheu um {forma} com perímetro de {perimetro}")
#Exercício 8
lados = int(input("Diga o número de lados: "))
if lados<3:
    print("Não é um polígono")
elif lados > 5:
    print("Polígono não identificado")
else:
    valor = int(input("Diga o tamanho do lado: "))
    if lados == 3:
        forma = 'triângulo'
    elif lados == 4:
        forma = 'quadrado'
    elif lados == 5:
        forma = 'pentágono'
    perimetro = lados*valor
    print(f"Você escolheu um {forma} com perímetro de {perimetro}")

#Exercício 10
lado1 = int(input("Diga o primeiro lado: "))
lado2 = int(input("Diga o segundo lado: "))
lado3 = int(input("Diga o terceiro lado: "))

if lado1 == lado3 and lado1 == lado2:
    print("Equilátero")
elif lado3 == lado2 or lado1 == lado3 or lado1 == lado2:
    print("Isósceles")
else:
    print("Escaleno")

#Exercício 11
ang1 = int(input("Diga o primeiro angulo: "))
ang2 = int(input("Diga o segundo angulo: "))
ang3 = int(input("Diga o terceiro angulo: "))
if ang3 + ang2 + ang1 == 180:
    if ang1 == 90 or ang2 == 90 or ang3 == 90:
        print("Retângulo")
    elif ang1 > 90 or ang2 > 90 or ang3 > 90:
        print("Obtuso")
    else:
        print("Agudo")
else:
    print("Vc nao manja triangulos")

#Exercício 9
a = int(input("Diga um numero: "))
b = int(input("Diga outro numero: "))
c = int(input("Diga outro numero: "))

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

maior = a
if b>maior:
    maior = b
if c>maior:
    maior = c
print(maior)
'''
a = int(input("Diga um numero: "))
b = int(input("Diga outro numero: "))
c = int(input("Diga outro numero: "))

if a > b and a > c:
    aux = a
    a = c
    c = aux
elif b > c:
    aux = b
    b = c
    c = aux
if a>b:
    aux = a
    a = b
    b = aux
print(a,b,c)

maior = a
if b>maior:
    maior = b
if c>maior:
    maior = c

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

meio = a + b + c - menor - maior
print(menor,meio,maior)
