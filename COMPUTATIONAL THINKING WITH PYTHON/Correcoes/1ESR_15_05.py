def verifica_numero(msg,msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    num = int(num)
    return num

def verifica_elemento(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return True
    return False

def forca_opcao(msg,msg_erro,lista_opcoes):
    opcao = input(msg)
    while not verifica_elemento(lista_opcoes,opcao):
        print(msg_erro)
        opcao = input(msg)
    return opcao


def acha_pares(lista_numeros):
    pares = []
    for elem in lista_numeros:
        if elem%2==0:
            pares.append(elem)
    return pares

#filtro_pares = acha_pares(lista)
#print(filtro_pares)
#lista_2 = [32,5,31,245,75,23,542,21,32,24]
#filtro_pares = acha_pares(lista_2)
#print(filtro_pares)
#carros = ['up','uno','celtinha brabo','gol']
#carro = forca_opcao("Qual carro lhe interessou?\n->",
#                    'Opção inválida',carros)
#print(carro)
#continuar_ou_nao = forca_opcao("Deseja continuar?",'(s/n)',['s','n'])
#print(continuar_ou_nao)
#x = verifica_numero("Diga um numero: ","Deve ser um numero!")
#print(x)
#y = verifica_numero("Diga a quantidade de garrafas: ",'A qtd é um numero')
#print(y)
def soma_lista(lista):
    soma = 0
    for elem in lista:
        soma += elem
    return soma

def acha_maior(lista):
    local_maior = 0
    maior = lista[local_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            local_maior = i
    return local_maior


lista = [2, 4, 76, 56, 98, 12]
indice_maior = acha_maior(lista)
print(indice_maior,lista[indice_maior])


