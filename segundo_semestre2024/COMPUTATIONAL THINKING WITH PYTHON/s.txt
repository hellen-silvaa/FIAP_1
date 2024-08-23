'''mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


lista = ['Dark Side of the Moon', 'Animals', 'The Wall']
for album in lista:
    print(album)

para um i em um range de 0 a 30 faça
lista = list(range(0, 30))
for i in lista:
    print(i)

s='the quick brown fox jumps over the lazy dog'
if 'a' in s:
    print('contido')
if '6' not in s:
    print('não está contido')

aluno_01 = 'Maria'
aluno_02 = 'João'
aluno_03 = 'Ana'
aluno_04 = 'Ótavio'

nome_aluno = ''

em vez de or usamos uma lista e in para verificar se esta na lista in

if nome_aluno in ['Maria', 'Ana']:
    print('Sexo feminino')

if nome_aluno in ['João', 'Ótavio']:
    print('Sexo masculino')
usamos not in para verificar se não esta na lista

usar in para verificar se se algum
elemento está contido ou não contido em uma string ou
lista:

s='the quick brown fox jumps over the lazy dog'
if 'a' in s:
    print('contido')
if '6' not in s:
    print('não está contido

-break interrompe o laço
-continue passa para a próxima iteração.

 O código dentro do else é executado
ao final do laço, a não ser que o laço tenha sido
interrompido por break.

for i in range(0, 30):
    if i == 15:
        break
    print(i)

for i in range(0,30):
    if i%2 !=0:
        continue
    print(i)


o else aqui não é do if o else é do for!!!!!!!!!!!

for i in range(0,30):
    if i == 40:
        print('Encontrei')
        break
else:
    print('Não Encontrei')


    Enumerate
Essa função pode receber como entrada uma lista e irá
retornar um objeto do tipo enumerate, que poderá ser
percorrido pelo for. Vejamos um exemplo simples:


for i,letra in enumerate(L):
    print(i,letra)


--------------aqui o enumerate pega uma coleção de elementos e da o número do indice dele------------------------

Lista = ['Banana', 'Abacaxi', 'Manga', 'Uva']

for i, fruta in enumerate(Lista):
    print(i, ':' , fruta)

A função zip() retorna um objeto zip, que é um iterador
de tuplas onde o primeiro item em cada iterador passado
é emparelhado e, em seguida, o segundo item em cada
iterador passado é emparelhado etc.
Se os iteradores passados tiverem comprimentos
diferentes, o iterador com menos itens decide o
comprimento do novo iterador

tuplas não da para alterar


a=("John", "Charles", "Mike")
b=("Jenny", "Christy", "Monica")

x = zip (a, b)
print(list(x))

---------------------------------------------------------------------------------

name, surname, number é a variavel que estou atribuindo pode ser qualquer nome

names = ['John', 'Robert']
surnames = ['Smith', 'De Niro']
numbers = [1, 2]

for name, surname, number in zip(names, surnames, numbers):
    print(name, surname, number)


for person in zip(names, surnames, numbers):
    print(person)

crie uma lista i ao quadrado e para cada i que estiver no range de uma lista de 0 a 100 print

quadrados = [i**2 for i in range(0, 101)]
print(quadrados)


crie uma lista i ao quadrado e para cada i que estiver no range de uma lista de 0 a 100 SE i > 10 print

quadrados = [i**2 for i in range(0, 101) if i > 10]
print(quadrados)

L = [value ** 2 for value in range (1, 11)]
print(L)

pares = [i for i in range (0, 101) if i % 2 == 0]
print(pares)

def gerar_lista_de_quadrados():
    Lista = []
    for i in range (0,100):
        Lista.append(i**2)
    return Lista

PESQUISAR FUNÇÃO LAMBDA
programação funcional: (mesma coisa que a de cima)
L = [value ** 2 for value in range (1, 101)]
print(L)

While
O laço for toma uma coleção de itens e executa um bloco
de código uma vez para cada item da coleção. Em
comparação, o laço while executa um bloco de código
enquanto uma determinada condição for verdadeira


currentNumber = 0

currentNumber = 0
while currentNumber <= 10:
    print(currentNumber)
currentNumber += 1

while True:
entrada = input('Digite algo: ')
    if entrada == 'quit':
        break
    else:
    print('O texto digitado foi: '+ entrada)

------------------Jogo de advinhar o número-----------------------
'''
import random

numero = random.randint(0,10)

while True:
    chute = int(input('Digite um chute: '))
    if chute == numero:
        print('Acertou miseravi')
        break
    print('Errouu')













