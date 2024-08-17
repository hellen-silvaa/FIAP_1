'''Tupla usa parênteses no lugar de colchetes, depois de definir a tupla, podemos acessar elementos individuais usando o índice '''

'''dimensions = (200, 400)
dimensions[0] = 100'''

alunos = ['João', 'Maria', 'Joãozinho', 'Mariazinha']
copia_alunos = list(alunos)
print(copia_alunos)

'''para cada 1 nno range de 0 a 9 faça alguma coisa com i'''
for i in range (0, 10):
    print(i)

''' EXERCÍCIO:  criar lista que guarda os numeros quadrados de 0 a 100 e usar o for para adiconar'''

num_quadrado = []
for i in range (0, 101):
    quadrado = i * i
    num_quadrado.append(quadrado)
print(num_quadrado)

'''quadrados apenas dos númersos pares'''

num_quadrado = []
for i in range (0, 101):
    if i % 2 == 0:
        num_quadrado.append(i**2)
print(num_quadrado)

num_quadrado = [i**2 for i in range(0,101) if i % 2 == 0]
print(num_quadrado)

'-------------------------------------------------------------------------------------------'
