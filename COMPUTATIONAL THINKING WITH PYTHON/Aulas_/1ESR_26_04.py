'''vinho1 = 'Chapinha'
preco1 = 10
qtd1 = 0
vinho2 = 'Sangue de Boi'
preco2 = 20
qtd2 = 0
vinho3 = 'Catuaba'
preco3 = 30
qtd3 = 0
valor = 0
frete = 10
print("Seja bem vindo à vinheria Agnello!!!!!!!!!")
ano = input("Diga seu ano de nascimento: ")
while not ano.isnumeric():
    ano = input("Diga seu ano de nascimento: ")
ano = int(ano)
idade = 2024 - ano
if idade >= 18:
    endereco = input("Diga seu endereço: ")
    while True:
        opcao = input(f"Qual vinho voce quer ?\n {vinho1} : {preco1}"
                      f"\n{vinho2} : {preco2}\n{vinho3} : {preco3}")
        while opcao != vinho1 and opcao != vinho2 and opcao != vinho3:
            print("Opção inválida!")
            opcao = input(f"Qual vinho voce quer ?\n {vinho1} : {preco1}"
                      f"\n{vinho2} : {preco2}\n{vinho3} : {preco3}")

        qtd = input(f"Qtos vinhos {opcao} ?")
        while not qtd.isnumeric():
            print("Deve ser um numero!")
            qtd = input(f"Qtos vinhos {opcao} ?")
        qtd = int(qtd)

        if opcao == vinho1:
            preco = qtd * preco1
            qtd1 += qtd
        elif opcao == vinho2:
            preco = qtd * preco2
            qtd2 += qtd
        else:
            preco = qtd*preco3
            qtd3 += qtd
        valor += preco
        resposta = input("Você quer comprar mais vinhos? (s/n)\n->")
        while not (resposta == 's' or resposta == 'n'):
            print("Opção inválida!")
            resposta = input("Você quer comprar mais vinhos? (s/n)\n->")
        if resposta == 'n':
            break
    if valor >= 500:
        print("Frete Grátis")
    else:
        valor += frete
    print(f"Obrigado por comprar aqui!!!!\n"
          f"Você comprou:\n{qtd1} de {vinho1}\n{qtd2} de {vinho2}\n"
          f"{qtd3} de {vinho3} por R${valor:.2f} e"
          f" será entregue em {endereco}")
else:
    print("Sai kids")
vogais = 0
for char in 'danilo':
    print(char)
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vogais += 1

for i in range(1,10,2):#start,end,step
    print(i)

for i in range(10):
    print(i,end = ' ')
    i = 1
    print(i)

senha_cadastrada = '1234'
for i in range(3):
    senha = input("Diga sua senha: ")
    if senha == senha_cadastrada:
        print("Acesso Liberado!")
        break
    print(f"Sai Hacker!!!!!! Só mais {2-i} tentativas!")
if senha != senha_cadastrada:
    print("Sai Hacker")

#peça 10 numeros ao usuario e conte a qtd de pares e impares
#peça 10 numeros ao usuario faça a media e a soma
#some todos os numeros de 1 a 100
#faça a tabuada de todos os numeros de 1 a 10

pares = 0
for i in range(1,11,1):
    num = input("Diga um numero: ")
    while not num.isnumeric():
        num = input("Diga um numero: ")
    num = int(num)
    if num % 2 == 0:
        pares += 1
print(f"{pares} pares e {i - pares} impares")
'''
frase = 'a materia de python é muito legauuuuu'
nome = 'danilo'
meu_len = 0
for char in nome:
    meu_len += 1
print(meu_len)







#def -> definindo função

#Função 1: pode votar
'''def podeVotar(nome, idade):
    if idade >= 16:
        print(f"Sim, a pessoa {nome} pode votar")
        return True
    else:
        print(f"Não, a pessoa {nome} ainda não pode votar")
        return False

a = podeVotar("Lucas",38)
print(f"a primeira resposta foi {a}")
b = podeVotar("Maira",13)
print(f"a segunda resposta foi {b}")
c = podeVotar("Pedro",18)



#Função 2: calcula idade
ano_atual = 2024
def calculaIdade(nome, ano_nascimento):
    idade = ano_atual-ano_nascimento
    print(f"A pessoa {nome} tem {idade} anos")
    return idade

a = calculaIdade ("João", 2004)
b = calculaIdade("Hellen", 2002)
c = calculaIdade("Maria", 2024)




Função 2.1: calcula idade para votar
def podeVotar(nome, ano_nascimento):
    idade = calculaIdade(nome, ano_nascimento)
    if idade >= 16:
        print(f"Sim, a pessoa {nome} pode votar")
        return True
    else:
        print(f"Não, a pessoa {nome} ainda não pode votar")
        return False

def calculaIdade(nome,ano_nascimento):
    print(f"A pessoa {nome} tem a idade {2024-ano_nascimento}")
    return 2024-ano_nascimento

a = podeVotar("Lucas",2004)
b = podeVotar("Rafael",1996)
c = podeVotar("Gabriela",2014)

#Função 2.2: calcula idade para votar
def calculaIdade(nome,ano_nascimento):
    idade  = 2024-ano_nascimento
    print(f"A pessoa {nome} tem a idade {idade}")
    return idade


a = calculaIdade("Lucas",2004)
b = calculaIdade("Rafael",1996)
c = calculaIdade("Gabriela",2014)


#Função 2.3: calcula idade para votar
from datetime import datetime

agora = datetime.now()
ano_atual = agora.year



def calculaIdade(nome,ano_nascimento):
    idade  = ano_atual-ano_nascimento
    print(f"A pessoa {nome} tem a idade {idade}")
    return idade


a = calculaIdade("Lucas",2004)
b = calculaIdade("Rafael",1996)
c = calculaIdade("Gabriela",2014)

from datetime import datetime

#escopo é igual conjunto de variaveis



#Função 2.4: calcula idade para votar

def podeVotar(nome, ano_nascimento):
    idade = calculaIdade(ano_nascimento)
    a = 12
    if idade >= 16:
        print(f"Sim, a pessoa {nome} pode votar")
        return True
    else:
        print(f"Não, a pessoa {nome} ainda não pode votar")
        return False

def calculaIdade(ano_nascimento):
    return 2024-ano_nascimento


a = podeVotar("Lucas",2004)
b = podeVotar("Rafael",1996)
c = podeVotar("Gabriela",2014)'''


#Funçao 3: Maior elemento de uma lista

def maior(numeros):
    maior = 0
    for elemento in numeros:
        if elemento > maior:
            maior = elemento
    return maior

n1 = maior([30,2,90,4,3])
n2 = maior([30,2,22,4,400])
print(n1)
print(n2)


#Funçao 3.1: Maior elemento de uma lista

def maior(numeros):
    maior = 0
    for elemento in numeros:
        if elemento >  maior:
            maior = elemento
    return maior


n = maior([10,20,2,30,7]) #maior retorna o 30, o n vai valer 30
n2 = maior([100,200,2,30,7]) #maior retorna o 200, o n vai valer 200
n3 = maior([-2,-3,-1]) #BUG! era pra ser -1, mas vai ser 0














