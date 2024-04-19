'''#Exercício 1
while True:
    nota = input("Diga sua nota: ")
    if nota.isnumeric():
        nota = int(nota)
        if nota <= 10:
            break
#Exercício 2
nome = input("Diga seu nome: ")
while len(nome) < 3:
    nome = input("Diga seu nome: ")

while True:
    idade = input("Diga sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade < 150:
            break
    print("Opção inválida")
salario = input("Diga seu salario: ")
while not salario.isnumeric():
    print("Opção inválida")
    salario = input("Diga seu salario: ")

.
sexo = input("Diga f ou m")
while not (sexo == 'f' or sexo == 'm'):#while sexo != "f" and sexo != "m":
    print("Opção inválida")
    sexo = input("Diga f ou m")

es = input("Diga seu estado civil (s,c,v ou d): ")
while not (es == 's' or es == 'c' or es == 'v' or es):
    print("Opção inválida")
    es = input("Diga seu estado civil (s,c,v ou d): ")

a = 80
b = 200
tempo = 0
while a < b:
    a*=1.03
    b*=1.015
    tempo+=1
print(tempo)

qtd = 0
soma = 0
while qtd < 5:
    num = input(f"Diga o {qtd+1}º numero: ")
    while not num.isnumeric():
        print("É número!")
        num = input(f"Diga o {qtd+1}º numero: ")
    num = int(num)
    soma += num
    qtd += 1
print(f"A soma é {soma}")
print(f"A media é {soma/qtd}")
'''
a = int(input("Diga um numero: "))
b = int(input("Diga outro numero: "))

while a<b:
    print(a)
    a+=1

while b < a:
    print(b)
    b+=1



6- #Ler nome de usuário e senha
user = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

#Criar uma validação para a senha ser diferente do nome de usuário
while senha == user:
    print("\nOPA! Sua senha e seu nome de usuário não podem ser iguais! Vamos trocar isso ai!\n")
    user = input("Digite um nome de usuário novo: ")
    senha = input("Digite uma senha diferente do seu nome de usuário: ")

print("\nCERTOOO!\n"
      f"Seu nome de usuário é: {user}\n"
      f"Sua senha é: {senha}\n")

7- ''' Gerando a tabuada 1 ao 10 sem pedir ao usuário um valor '''
#Inicia com 0
n = 0
#Enquanto o n(1) for menor que 10:
while n <= 10:
    i = 0
    #Enquanto o múltiplo for menor que 10:
    while i <= 10:
        #Printa a conta:
        print(f"{n} * {i} = {n*i} ")
        #Adiciona um a repetição
        i += 1
    #Adiciona um ao número
    n += 1
    print("-------")

'''
RESOLUÇÃO DO PROFESSOR
a = 1
b = 2
 
i = 2
n = 17
print(a)
print(b)
 
while i < n:
    c = a + b
    a = b
    b = c
    print(c)'''

'''i = 0
pares = 0
while i <10:
    num = input(f'Diga o {i+1} numero: ')
    while not num.isnumeric():
        print("Tem que ser um número!!!")
        num = input("Diga um numero: ")
    num = int(num)
    if num % 2 == 0:
        pares += 1
        continue
#continue -> pule esse passo do loop ele pula tudo (oposto do breack)
    i += 1
print(f"{pares} pares e {i-pares} impares")


#10 fatorial

num = 5
fatorial = num
fatorial_sting = f"{num}! = {num}"
while num > 1:
    num -=1
    fatorial *= num
    fatorial_sting += f"*{num}"
fatorial_sting += f"*{fatorial}"
print(fatorial_sting)'''

#11

num = 7
i = 2
while i < num/2:
    print(f"{num}%{i}={num%i}")
    if num % i == 0:
        print(f"{num} não é primo")
        break
    elif i == num-1:
        print(f"{num} é primo")
        break
    i +=1
if i >= num*0.5:
    print(f"{num} é primo")

#só precisa testar até a raiz quadrada do numero para saber se é ou não primo
# raiz quadrada é numero elevado a meio (numero*0.5)


#12 é igual o 4
#13 parece o da população taxa varia
#14

salario = 1000
partida = 1995
taxa = 0.015
while partida < 2024:
    salario *= 1 + taxa
    taxa *= 2
    partida += 1
    print(salario)

















#14 -> 14 - Faça um programa que leia uma quantidade indeterminada de números positivos e
#conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
#A entrada de dados deverá terminar quando for lido um número negativo.

'''primeiro = 0
segundo = 0
terceiro = 0
quarto = 0

while True:
    num = input("Diga um numero\n->")
    if num.isnumeric():
        num = int(num)
        if num <= 25:
            primeiro += 1
        elif num <= 50:
            segundo += 1
        elif num <= 75:
            terceiro += 1
        elif num <= 100:
            quarto += 1
        else:
            break
    else:
        print("É um número manooo")
print(f"Há {primeiro} números no primeiro intervalo\n"
    f"Há {segundo} números no segundo intervalo\n"
    f"Há {terceiro} números no terceiro intervalo\n"
    f"Há {quarto} números no quarto intervalo")
'''


'''15 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados 
por meio de código. Os códigos utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o 
conjunto de votos tem-se o valor zero'''

danilo = 0
abner = 0
catroppa = 0
Neugeb = 0
voto = 0
nulos = 0
branco = 0
total = 0
while True:
    voto = input ("Diga seu voto:\n1 - Danilo\n2 - Abner"
                  "\n3 - Catroppaz\n4 - Neugeub"
                  "\n0 - Sair\n0 o futuro do Brasil depende de você!->")

    if not (voto == '0' or voto == '1' or voto == '2' or voto == '3' or
             voto == '4' or voto == '5' or voto == '6'):

        print("Errou!")
        continue

    if voto == '0':
        break
    elif voto == '1':
        danilo += 1
    elif voto == '2':
        abner += 1
    elif voto == '3':
        catroppa += 1
    elif voto == '4':
         Neugeb += 1
    elif voto == '5':
        nulos += 1
    elif voto == '6':
        branco += 1
        total +=1

if total != 0:
    print(f"Danilo receberu {danilo} votos \n"
      f"abner receberu {abner} votos \n"
      f"catroppa receberu {catroppa} votos \n"
      f"neugeb receberu {Neugeb} votos \n"
      f"branco receberu {branco} votos \n"
      f"porcentagem {100*nulos/total:.2f}% votos \n"
      f"porcentagem {100*branco/total:2f}% votos \n")

#while true ->

#garantir que é um numero em um certo intervalo -> isnumeric
'''while not num.isnumeric():
    num = input("Diga um número: ")
    
    while True:
        num = input("Diga um número: ")
        if num.isnumeric():
            break'''








