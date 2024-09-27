'''Exercício 1
Você está desenvolvendo um sistema de análise de notas de alunos em diferentes
disciplinas. Cada linha da matriz representa um aluno e cada coluna representa
uma disciplina. Escreva um programa que calcule a média de notas de cada aluno.
# Exemplo de entrada:
# Matriz de notas:
# [ [8, 7, 9], # Notas do Aluno 1 (Matemática, Português, História)
# [6, 8, 7], # Notas do Aluno 2 (Matemática, Português, História)
# [9, 9, 10]] # Notas do Aluno 3 (Matemática, Português, História)
# Exemplo de saída:
# Média de cada aluno:
# Aluno 1: 8.0
# Aluno 2: 7.0
# Aluno 3: 9.

média -> soma tudo e divide pelo total'''
'''

import numpy as np

#matriz de notas com numpy

notas = np.array([ [8, 7, 9],
                        [6, 8, 7],
                        [9, 9, 10] ])


medias = np.mean(notas, axis=1)

print(medias)'''

'''import numpy as np

notas =  [[8, 7, 9],
        [6, 8, 7],
        [9, 9, 10]]

medias = []

for aluno in notas:
    medias.append(sum(aluno)/len(aluno))

print (medias)'''

#------------------------------------------------------------------------------------------------------------
'''Exercício 2
Crie um gráfico de barras para representar a média de cada aluno do exercício
anterior.'''

from matplotlib import pyplot as plt
import numpy as np


notas =  [[8, 7, 9],
        [6, 8, 7],
        [9, 9, 10]]

medias = []
alunos = ['Aluno1','Aluno2', 'Aluno3']


for aluno in notas:
    medias.append(sum(aluno)/len(aluno))

print (medias)

plt.bar(alunos, medias, color = ['r', 'b', 'y'] )
plt.title('Média dos alunos')

plt.show()

#------------------------------------------------------------------------------------------------------------
'''Exercício 3
Devido à covid as cadeiras de cinema têm que ser utilizadas com um espaçamento
de uma cadeira desocupada tanto na frente quanto atrás e dos lados. Represente
está situação com uma matriz 50x50 em que cada local (i,j) tem nele a palavra
“vaga” ou ocupada.'''

from matplotlib import pyplot as plt
import numpy as np

'''matriz = np.zeros ((50,50))


for linha in matriz:
    print(linha)'''
                                #colunas            #linhas
lugares = [['ocupado' for _ in range(50)] for i in range(50)]

#enumerate conta cada elemento(n) em
for n, fileira in enumerate(lugares):
    for i in range(len(fileira)):
        if i in range(len(fileira)):
            if i % 2 == 0 and n % 2 == 0:
                fileira[i] = 'vago'

for fileira in lugares:
    print(fileira)

#------------------------------------------------------------------------------------------------------------
'''Exercício 4
Crie uma variação do exercício anterior usando o matplot lib que vai gerar uma
imagem com representando as cadeiras. Locais ocupados serão representados por
um quadrado preto e locais disponíveis por um quadrado branco.'''

import numpy as np
import matplotlib.pyplot as plt

                                #colunas            #linhas
lugares = [[0 for _ in range(10)] for i in range(10)]

#enumerate revisar
for n, fileira in enumerate(lugares):
    for i in range(len(fileira)):
        if i in range(len(fileira)):
            if i % 2 == 0 and n % 2 == 0:
                fileira[i] = 1

'''for fileira in lugares:
    print(fileira)'''

cmap = plt.get_cmap('Reds')
plt.imshow(lugares, cmap= cmpa, interpolation='none')
plt.axis('off')
plt.title('Lugares')
plt.show()

#------------------------------------------------------------------------------------------------------------
