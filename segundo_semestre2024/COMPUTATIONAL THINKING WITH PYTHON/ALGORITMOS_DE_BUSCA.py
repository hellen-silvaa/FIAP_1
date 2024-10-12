def ramdom_list():
    lista = []
    for i in range(1000000):
        lista.append(random.randint(0, 99999))
    return lista



def busca_sequencial(lista, e):
    operacoes = 0
    for i in lista:
        operacoes += 1
        if i == e:
            print('O elemento está na lista')
            print(f'Operações: {operacoes}')
            return
    print('O elemento está na lista')
    print(f'Operações: {operacoes}')

lista = [1,2,3,4,5,6,7,8,9,10]


def pesquisa_binaria(lista, item):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
      meio = (esquerda + direita) // 2
    if lista[meio] == item:
        return meio
    elif lista[meio] > item:
        direita = meio - 1
    else:
        esquerda = meio + 1
    return -1
