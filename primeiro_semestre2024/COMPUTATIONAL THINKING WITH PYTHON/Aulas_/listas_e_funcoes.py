
'''1. Escreva uma função que recebe uma lista de números e retorna a soma de
todos os elementos da lista.

def soma(lista):
    return sum(lista)

n1=[1,2,3,4,5]
print(f' A soma dos elementos da lista é {soma(n1)}')'''


'''2. Crie uma função que recebe uma lista de números e retorna o maior elemento
da lista.'''


def maior(numeros):
    maior = 0
    for elemento in numeros:
        if elemento > maior:
            maior = elemento
    return maior

lista1 = maior([30,2,90,4000,300,800])
lista2 = maior([30,2,22,4,400,8000,40])
print(f'O maior elemento da lista 1 é {lista1}')
print(f'O maior elemento da lista 2 é {lista2}')

3. Faça uma função que recebe uma lista de strings e retorna uma nova lista
contendo apenas as strings que começam com a letra 'a'.
4. Escreva uma função que recebe uma lista de números e retorna uma nova
lista contendo apenas os números pares.
5. Crie uma função que recebe uma lista de palavras e retorna o número de
letras em cada palavra como uma nova lista.
6. Faça uma função que recebe duas listas e retorna uma lista contendo os
elementos comuns entre as duas listas.
7. Escreva uma função que recebe uma lista de números e retorna True se a
lista estiver em ordem crescente e False caso contrário.
8. Crie uma função que recebe uma lista de números e retorna uma nova lista
com os elementos em ordem inversa.
9. Faça uma função que recebe uma lista de strings e retorna uma nova lista
contendo as mesmas strings, mas em ordem alfabética.
10.Escreva uma função que recebe uma lista de números e retorna a média
aritmética dos elementos da lista.'''
