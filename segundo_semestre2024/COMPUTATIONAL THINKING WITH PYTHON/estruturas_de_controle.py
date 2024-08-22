'''number = int(input('Digite um número: '))
if number > 6:
    print('maior que 6')
else:
    (print('O número é menor que 6'))'''

'''print( 1> 2 )
print("a" > "b")
print(5 < 10)
print(200 == 200)
print("" == "")'''

'''nome = 'a'
if nome:
    print('verdadeiro')'''

'''Por causa da tabela unicode le considera
 a ordem da mesma, por isso o b é maior que a

print(ord('A'))
print(ord('B'))


nota = int(input('Digite a sua nota: '))
if nota >=6:
    print('Aprovado')
elif nota >=5:
    print('Exame')
else:
    print('Reprovado')
'''

a = True
b = False

'''ele sempre faz o and primeiro por procedencia
if a or b and b:
    print(True)
else:
    print(False)

if a and b and b:
    print(True)
else:
    print(False)
'''

'''------------------------------------------------------------'''
'''Operador Ternário:

x = 2
if x == 2:
    print('deu certo')
else:
    print('deu errado')

x = 2
print('deu certo') if x == 2 else print('deu errado’)
'''


'''------------------------------------------------------------'''
'''Match-case: 
é uma estrutura de controle de fluxo que comparar uma variável com diferentes valores
ou padrões de forma mais organizada e legível
    _ é usado quando não entra em nenhum caso

opcao = 'a'

match opcao:
    case 'a':
        print("Opção A selecionada")
    case 'b':
        print("Opção B selecionada")
    case _: print("Opção inváliada")


- Legibilidade: O código fica mais claro e fácil de entender.
- Flexibilidade: Permite testar valores alternativos em um mesmo
case usando o operador |.
- Padrões Estruturais: Pode verificar o tipo de dado e buscar
por padrões estruturais dentro da variável.'''

'''Comparando Strings

nome = "João"

match nome:
    case "João":
        print("Olá, João!")
    case "Maria":
        print("Olá, Maria!")
    case _:
        print("Não reconheço você!")
        
        
variavel = 123
match variavel:
    case int():
        print("A variável é um inteiro")
    case str():
        print("A variável é uma string")
    case _:
        print("Tipo de dado não identificado")



Usando Padrões Estruturais
dados = {'nome': 'João', 'nota': 10}
    match dados:
    case {'nome': 'João', 'nota': 10}:
        print("João tirou nota 10")
    case _:
        print("Nenhuma informação obtida")





def describe_fruit(fruit):
    match fruit:
        case "maçã" | "banana" | "laranja":
            print("Esta é uma fruta comum.“)
        case "manga" | "abacaxi":
            print("Esta é uma fruta tropical.")
        case _:
            print("Fruta desconhecida.")
            
Uso do if no case

number = 8
    match number:
    case x if x < 0:
        print("Número negativo")
    case x if x == 0:
        print("Zero")
    case x if x > 0 and x < 10:
        print("Número pequeno positivo")
    case x if x >= 10:
        print("Número grande positivo")
    case _:
        print("Valor desconhecido")
        
        Pattern matching
point = (4, 0)
match point:
    case (0, 0):
        print("O ponto está na origem.")
    case (x, 0):
        print(f"O ponto está no eixo X em ({x}, 0).")
    case (0, y):
        print(f"O ponto está no eixo Y em (0, {y}).")
    case (x, y):
        print(f"O ponto está em ({x}, {y}).")
    case _:
        print("Formato de ponto desconhecido.")
'''

'''
lista = [a, 0, 'aa', 54, 'bb']
match lista:
    case []:
        print("A lista está vazia.")
    case [single]:
        print(f"A lista contém um único elemento: {single}.")
    case [first, second]:
        print(f"A lista contém dois elementos: {first} e {second}.")
    case [first, *middle, last]:
        print(f"A lista tem vários elementos. Primeiro: {first}, último: {last}, e os do meio: {middle}.")
    case _:
        print("Formato de lista desconhecido.")

Pattern matching

match dictionary:
# pattern 1
    case {"name": n, "age": a}:
        print(f"Name:{n}, Age:{a}")
# pattern 2
    case {"name": n, "salary": s}:
        print(f"Name:{n}, Salary:{s}")
# default pattern
    case _ :
        print("Data does not exist")


'''
