#


'''def criar_matriz_zeros(m, n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz.append(linha)
    return matriz'''

'''def print_matriz(matriz):
    for linha in matriz:
        print(linha)

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]
def matriz_diagonal(matriz):
    m = len(matriz)
    for i in range(m):
        matriz[i][i] = 1

    return  matriz
'''

print(matriz_diagonal(matriz))


'''correção python'''


def criar_matriz_zeros(m, n):
# Cria uma matriz com m linhas e n colunas, preenchida com zeros
    matriz = [[0 for _ in range(n)] for _ in range(m)]
    return matriz

def diagonal_principal(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1

matriz = criar_matriz_zeros(9,9)
diagonal_principal(matriz)

for linha in matriz:
    print(linha)














''''      0  1   2    0  1   2    0  1   2
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
             1          2           3            '''

def criar_matriz_zeros(m, n):
# Cria uma matriz com m linhas e n colunas, preenchida com zeros
    matriz = [[0 for _ in range(n)] for _ in range(m)]
    return matriz

def diagonal_contra(matriz):
    size = len(matriz)
    for i in range(size):
        matriz[i][size -1 - i] = 1

matriz = criar_matriz_zeros(9,9)
diagonal_contra(matriz)

for linha in matriz:
    print(linha)










def criar_matriz_zeros(m,n):
    matriz = [[0 for _ in range(n)] for _ in range(m)]
    return matriz

def diagonal_total(matriz):
    size = len(matriz)
    for i in range(size):
        matriz[i][i] = 1

matriz = criar_matriz_zeros(9,9)
diagonal_total(matriz)

for linha in matriz:
    print(linha)





