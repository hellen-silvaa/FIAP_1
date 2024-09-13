''''#nuypay gera matrizes
#lista encadeada matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

def criar_matriz_zeros (m, n):
    #iniciando uma matriz vazia
    matriz = []

    #loop para criar m linhas
    for i in range(m):
        linha = [] #cria uma nova linha vazia
        #loop para adicionar n zeros na linha
        for j in range(n):
            linha.append(0)
            #adiciona a linha criada a matriz
        matriz.append(linha)
    return matriz
def print_matriz(matriz):
    for linha in matriz:
        print(linha)

matriz = criar_matriz_zeros(9,9)
print_matriz(matriz)


def criar_matriz_zeros(m, n):
    # Cria uma matriz com m linhas e n colunas, preenchida com zeros
    matriz = [[0 for _ in range(n)] for _ in range(m)]
    return matriz

def print_matriz(matriz):
    for linha in matriz:
        print(linha)

matriz = criar_matriz_zeros(9,9)
print(matriz)


#geração de imagens com matriz no pc o pixel biblioteca especifica
#regra de klamer resolver sistema de equação

def soma_matrizes(matriz1, matriz2):
    m = len(matriz1) # Número de linhas
    n = len(matriz1[0]) # Número de colunas
    resultado = criar_matriz_zeros(m, n)
    for i in range(m):
        for j in range(n):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]
    return resultado

def print_matriz(matriz):
    for linha in matriz:
        print(linha)

matriz = criar_matriz_zeros(9,9)
print(matriz)

# Exemplo
matriz1 = [[1, 2],
           [3, 4]]

matriz2 = [[5, 6],
          [7, 8]]
soma = soma_matrizes(matriz1, matriz2)




def multiplicar_matrizes (matriz1, matriz2):
    m = len(matriz1)
    n = len(matriz2[0])
    p = len(matriz2)

    resultado = criar_matriz_zeros(m,n)

    for i in range(m):
        for j in range(n):
            for k in range(p):
                resultado[i][j] += matriz1[i][j] * matriz2[k][j]
    return resultado

matriz1 = [[1,2],
           [3,4]]
matriz2 = [[5,6],
          [7,8]]

def transpor_matriz(matriz):
m = len(matriz)
n = len(matriz[0])
resultado = criar_matriz_zeros(n, m)
for i in range(m):
for j in range(n):
resultado[j][i] = matriz[i][j]
return resultado
# Exemplo
matriz = [[1, 2, 3],
[4, 5, 6]]
transposta = transpor_matriz(matriz)'''
#sempre que o i for igual ao j ele é igual
#matriz manipulação de imagem monitor

#lista encadeada matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

'''1 - Faça uma função que recebe uma matriz
quadrada como parâmetro e altera todos os
elementos da diagonal para 1.'''

def criar_matriz_zeros (m, n):
    matriz = []

    for i in range(m):
        linha = []

        for j in range(n):
            linha.append(1)

        matriz.append(linha)
    return matriz
def print_matriz_quadrada(matriz):
    for linha in matriz:
        print(linha)

matriz = criar_matriz_zeros(3,3)


def criar_matriz_um(param, param1):
    pass


matriz_quadrada = criar_matriz_um(1,1)
print_matriz_quadrada(matriz)
