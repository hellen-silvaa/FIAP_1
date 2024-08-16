'''Em Python, colchetes ([]) indicam uma lista, e elementos
individuais da lista são separados por vírgulas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)'''

'''----------------------------------------------------------------------'''

'''Para acessar um elemento de uma lista, escreva o nome da 
lista seguido do índice do item entre colchetes.
print(bicycles[0])'''

'''----------------------------------------------------------------------'''

'''O método append() facilita criar listas dinamicamente. Por
exemplo, podemos começar com uma lista vazia e então
acrescentar itens à lista usando uma série de instruções
append()

bicycles.append('Alex')
print(bicycles)'''

'''----------------------------------------------------------------------'''
'''Você pode adicionar um novo elemento em qualquer posição de
sua lista usando o método insert(). Faça isso especificando
o índice do novo elemento e o valor do novo item.


bicycles.insert(1,'Ducati')
print(bicycles)'''



'''----------------------------------------------------------------------'''
'''del é função do python que você passa um indice para ele remover e o remove é uma função da lista e chama como removedor de ponto'''
'''Para remover um determinado item da lista, use o comando del e remove:

del bicycles[0]
print(bicycles)'''

'''----------------------------------------------------------------------'''
'''O método remove() apaga apenas a primeira ocorrência do
valor que você especificar.'''

'''bicycles.remove('Ducati')
print(bicycles)'''

'''----------------------------------------------------------------------'''


'''----------------------------------------------------------------------'''

'''As vezes, você vai querer usar o valor de um item depois de
removê-lo de uma lista.O método pop() remove o último item de uma lista, mas permite que você trabalhe com esse item depois da remoção.'''

'''bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles.pop())
print(bicycles)'''

'''----------------------------------------------------------------------'''
'''O termo pop deriva de pensar em uma lista como se fosse uma
pilha de itens e remover um item (fazer um pop) do topo da
pilha. Nessa analogia, o topo da pilha corresponde ao final
da lista'''

'''comidas = ['Lasanha', 'Pizza', 'Chocolate', 'Macarrão', 'jilo', '']
print(comidas.pop(0))
print(comidas)'''

'''----------------------------------------------------------------------'''

'''comidas = ['Lasanha', 'Pizza', 'Chocolate', 'Macarrão', 'jilo', '']
comidas.sort(reverse=True)
print(comidas)'''

'''---------------------------------------------------------------------'''
'''mostra ordenado mas não ordena altera a lista'''

'''comidas = ['Lasanha', 'Pizza', 'Chocolate', 'Macarrão', 'jilo', '']
comidas(sorted(comidas))
print(comidas)'''


'''----------------------------------------------------------------------'''

'''comidas_ordenadas = sorted(comidas)
print(comidas_ordenadas)
print(comidas)'''

'''----------------------------------------------------------------------'''
'''Também podemos ordenar essa lista em ordem alfabética
inversa, passando o argumento reverse=True ao método sort(). '''

'''cars = ['Ford', 'BMW', 'Audi']
cars.sort(reversed=True)
print(cars)'''

'''----------------------------------------------------------------------'''

'''para preservar a ordem original de uma lista, mas apresentá la de forma ordenada, podemos usar a função sorted(). A
função sorted() permite exibir sua lista em uma ordem em
particular, mas não afeta a ordem propriamente dita da
lista. (Essa função também aceita Reverse=True)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)'''
'''----------------------------------------------------------------------'''
'''numeros = [76,45,50,666, 50.7]
print(sum(numeros))

numeros = [76,45,50,666, 50.7]'''

'''----------------------------------------------------------------------'''

letras = list('the quick brown fox jumps over the lazy dog')
print(letras)

''' primeiro elemento -> onde começa a coleção
    segundo elemento -> até onde ele vai segundo valor (nocaso vai até o 99)
    terceiro elemento de quantos em quantos ele vai pular (padrão é 1)'''

numeros = list(range(0,100,2))
print(numeros)
'''----------------------------------------------------------------------'''

'''Podemos rapidamente descobrir o tamanho de uma lista usando
a função len().
cars = ['bmw', 'audi', 'toyota', 'subaru']print(len(cars)
'''

'''----------------------------------------------------------------------'''

'''Algumas funções Python são específicas para listas de
números. Por exemplo, podemos encontrar facilmente o valor
mínimo, o valor máximo e a soma de uma lista de números:

L=list(range(0,10))
print(min(L))
print(max(L))
print(sum(L))
'''

'''----------------------------------------------------------------------'''

cars = ['Ford', 'BMW', 'Audi']
copia_cars = cars

cars.pop()
print(cars)
print(copia_cars)

'''----------------------------------------------------------------------'''

'''Função Range A função Python range() retorna um conjunto de números sequenciais. Ela contém os parâmetros start, stop e 
step, que permitem configurar o retorno do intervalo de 
diferentes maneiras, como valores múltiplos de um 
determinado número e até intervalos com números 
negativos e positivos.'''

'''lista = list(range(0, 7))
print(lista)


lista = list(range(0, 30, 3))
print(lista)'''


'''----------------------------------------------------------------------'''

'''fatiamento pega todos valores da lista inicial começa no primeiro e termina no ultimo'''

cars = ['Ford', 'BMW', 'Audi']
copia_cars = cars[:]
cars.pop()
print(cars)
print(copia_cars)

'''----------------------------------------------------------------------'''

'''tracks = ['breath', 'on the run', 'time', 'the great gig in the sky', 'money',
'us and then', 'any colour you like', 'brain damage', 'eclipse']
lista = tracks
print(lista)
tracks.remove('breath')
tracks.remove('on the run')
print(lista)

Qualquer alteração na primeira lista também irá alterara 
segunda lista, porque na verdade lista está pontando para 
tracks!.
Para copiar uma lista, podemos criar uma fatia que inclua 
a lista original inteira omitindo o primeiro e o segundo 
índices ([:]). Isso diz a Python para criar uma lista que 
começa no primeiro item e termina no último, gerando uma 
cópia da lista toda.

'''

'''----------------------------------------------------------------------'''

'''tracks = ['breath', 'on the run', 'time', 'the great gig in the sky', 'money',
'us and then', 'any colour you like', 'brain damage', 'eclipse']
lista = tracks[:]
print(lista)
tracks.remove('breath')
tracks.remove('on the run')
print(lista)'''

'''----------------------------------------------------------------------'''

