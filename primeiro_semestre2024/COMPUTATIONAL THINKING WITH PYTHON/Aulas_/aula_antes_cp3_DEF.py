'''
ano = input("Diga seu ano de nascimento: ")
while not ano.isnumeric():
    ano = input("Diga seu ano de nascimento: ")
ano = int(ano)

qtd = input("Diga seu ano de nascimento: ")
while not ano.isnumeric():
    qtd = input("Diga seu ano de nascimento: ")
qtd = int(ano)

função -> bloco de código reutilizavel
parametrização
a mensagem que mdua a cada chamada e colocamos um parametro pra ela
'''
'''
#chamamos uma função dentr ode outra função
def verifica_numero(msg, msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    num = int(num)
    return num

def verifica_elemento(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return True
    return False'''

#a ordem dos parametros importa cada parametr osepara por virgula
'''
def forca_opcao(lista_opcoes, msg, msg_erro):
    opcao = input(msg)
    while not verifica_elemento(lista_opcoes, opcao):
        print(msg_erro)
        opcao = input(msg)
    return opcao

lista = [2,4,1,76,3,56,98,12,31,73]
def acha_pares(lista_numeros):
    pares = []
    for elem in lista_numeros:
        if elem%2==0:
            pares.append(elem)
    return pares
lista = [2,4,1,76,3,56,98,12,31,73]
filtro_pares = acha_pares(lista)
print(filtro_pares)
lista_2 = [32,5,31,245,75,23,542,21,32,24]
filtro_pares = acha_pares(lista_2)
print(filtro_pares)
'''




# importante: i = range associar i é para indice


#função que recebe lista de numeros e retorna a soma dos numeros

'''def soma_lista(lista):
    soma = 0
    for elem in lista:
        soma += elem
    return soma

lista = [2,4,1,76,3,56,98,12,31,73]

    local_maior = 0
    maior = lista[local_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            local_maior= i
    return local_maior

lista = [2,4,76,56,98,12]
indice_maior = acha_maior(lista)
print(indice_maior, lista[indice_maior])

'''

#if e else somente quando é excludente
#maior só muda o valor quando entra no if se não ele vai ser maior para sempre
'''
a = 1, b= 3, c =2, d=4

maior = a
if b > maior 
    maior = b
if c > maior 
    maior = c
if d > maior 
    maior = d
passa do presuposto que o maior é o primeiro faz o for com if'''







#carros= ['up', 'uno', 'celtinha brabo', 'gol']
#carro = forca_opcao("Qual carro lhe interessou?\n->",
                    #'Opção inválida', carros)
#print(carro)
#continuar_ou_nao = forca_opcao("Deseja continuar?" , '(s/n)',['s','n'])
#print(continuar_ou_nao)





#x = verifica_numero("Diga um número: " , "Deve ser um numero")
#print(x)
#y = verifica_numero("Diga a quantidade de garrafas: ",  "A qtd é um número")
#print(y)




def acha_maior(lista):
    local_maior = 0
    maior = lista[local_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            local_maior= i
    return local_maior

lista = [2,4,76,56,98,12]
indice_maior = acha_maior(lista)
print(indice_maior, lista[indice_maior])
