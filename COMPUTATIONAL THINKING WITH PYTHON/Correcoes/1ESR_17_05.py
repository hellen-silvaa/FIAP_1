def meu_reverse(lista):
    for i in range(len(lista)//2):
        ultimo = len(lista) - 1
        aux = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = aux
    return lista
'''
lista = [1,2,3,4,5,6,7,8,9]
lista2 = lista[:]
meu_reverse(lista2)
print(lista2)
print(4/3,4//3)
print(9/2,9//2)
print(lista)
'''
def soma_lista(lista):
    soma = 0
    for elem in lista:
        soma += elem
    return soma

def media_lista(lista):
    soma = soma_lista(lista)
    media = soma/len(lista)
    return media

def meu_in(lista,buscar):
    for elem in lista:
        if elem == buscar:
            return True
    return False

def meu_index(lista,buscar):
    for i in range(len(lista)):
        if lista[i] == buscar:
            return i
    return False

def forca_opcao(msg,lista_opcoes):
    msg_erro = ' '.join(lista_opcoes)
    msg_erro = f"Somente essas opcoes:\n{msg_erro}"
    opcao = input(msg)
    while not meu_in(lista_opcoes,opcao):
        print(msg_erro)
        opcao = input(msg)
    return opcao
def verifica_numero(msg):
    num = input(msg)
    if not num.isnumeric():
        print("Deve ser um numero!")
        num =  verifica_numero(msg)
    return int(num)
'''
num = verifica_numero('diga um numero: ')
print(num)
carros = ['up','uno','celtinha brabo','gol','kombi']
preco = [10,15,1000000,50,5]
escolha = forca_opcao("Diga um carro: ",carros)
indice_escolha = meu_index(carros,escolha)
valor_escolha = preco[indice_escolha]
print(f"O {carros[indice_escolha]} custa {preco[indice_escolha]}")
sim_ou_nao = ['sim','não']
escolha = forca_opcao("Voce quer continuar? ",sim_ou_nao)
'''
