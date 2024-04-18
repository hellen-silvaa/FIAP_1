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




