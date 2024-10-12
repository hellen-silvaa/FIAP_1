'''Uma função pode receber entradas (chamadas de
parâmetros ou argumentos), processar essas
entradas e retornar um resultado. Funções são
definidas usando a palavra-chave def, seguida
pelo nome da função, uma lista de parâmetros
entre parênteses e um bloco de código indentado
que representa o corpo da função.


def saudacao(nome):

Esta função recebe um nome e imprime uma mensagem de saudação.

print(f"Olá, {nome}!")
# Chamando a função
saudacao("Maria")

Argumentos posicionais
def somar(a, b):
return a + b
resultado = somar(3, 5)
print(resultado) # Saída: 8



Listas e Dicionários como Argumentos:

def somar(a, b, c):
    return a + b
args = [3, 5]
resultado = somar(*args) # Usa * para desempacotar a lista
print(resultado) # Saída: 8
kwargs = {'a': 3, 'b': 5}
resultado = somar(**kwargs) # Usa ** para desempacotar o dicionário
print(resultado) # Saída: 8



def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")
# Chamadas da função
saudacao("Maria") # Saída: Olá, Maria!
saudacao("João", "Oi") # Saída: Oi, João!
Múltiplos Valores Default
def criar_usuario(nome, idade=18, cidade="São Paulo"):
print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
# Chamadas da função
criar_usuario("Ana") # Saída: Nome: Ana, Idade: 18, Cidade: São Paulo
criar_usuario("Pedro", 25) # Saída: Nome: Pedro, Idade: 25, Cidade: São Paulo
criar_usuario("Clara", 30, "Rio de Janeiro") # Saída: Nome: Clara, Idade: 30,
#Cidade: Rio de Janeiro

Evitando que uma função modifique uma lista
Quando passamos uma lista para uma função, ela pode
ser modificada. Qualquer alteração feita na lista no
corpo da função é permanente (vai alterar a lista
original), já que quando passamos um objeto como
parâmetro, sempre passamos o endereço desse objeto, e
não os seus valores.
nome_da_função(nome_da_lista[:])

def soma_total(*numeros):
    print(numeros)
"""
Esta função aceita um número arbitrário de argumentos e retorna a soma de
todos.
"""
    return sum(numeros)
# Chamadas da função
print(soma_total(1, 2, 3)) # Saída: 6
print(soma_total(10, 20, 30, 40)) # Saída: 100
print(soma_total()) # Saída: 0


def exibir_informacoes(**informacoes):

    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")
# Chamadas da função
exibir_informacoes(nome="Ana", idade=25, cidade="São Paulo")
# Saída:
# nome: Ana
# idade: 25
# cidade: São Paulo
exibir_informacoes(produto="Notebook", preco=2500.00, marca="Dell")
# Saída:
# produto: Notebook
# preco: 2500.0
# marca: Dell
exibir_informacoes(pessoa="Hellen", status="Milionaria")
# Saída:
# pessoa: Hellen
# status: Milionaria

def combinar_argumentos(*args, **kwargs):

#Esta função aceita tanto argumentos posicionais quanto nomeados.

    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)
# Chamadas da função
combinar_argumentos(1, 2, 3, nome="Ana", idade=25)
# Saída:
# Argumentos posicionais: (1, 2, 3)



Eval
O eval é uma função embutida em Python que avalia
uma expressão em forma de string como código
Python. Em outras palavras, eval pega uma string
que representa uma expressão válida em Python e a
executa como se fosse código real. O resultado da
execução é retornado como o valor da expressão.

Como eval Funciona:
expression: A string que contém a expressão a ser avaliada.
globals (opcional): Um dicionário que define o escopo global para
a execução da expressão.
locals (opcional): Um dicionário que define o escopo local para a
execução da expressão.

# Definindo uma expressão matemática em forma de string
expressao = "2 + 3 * 5"
# Usando eval para avaliar a expressão
resultado = eval(expressao)
# Exibindo o resultado
print(resultado) # Saída: 17


# Definindo algumas variáveis
x = 10
y = 5
# Definindo uma expressão que usa essas variáveis
expressao = "x * y + 2"
# Usando eval para avaliar a expressão
resultado = eval(expressao)
# Exibindo o resultado
print(resultado) # Saída: 52



Exec
A função exec em Python é usada para executar
código Python dinâmico, ou seja, código que é
gerado ou definido em tempo de execução. Ao
contrário de eval, que é restrito a expressões
simples e retorna um valor, exec pode executar
qualquer código Python válido, incluindo
declarações, loops, definições de funções, classes,
e muito mais.

Nota: O uso de eval pode ser perigoso,
especialmente com entradas não confiáveis, pois ele
executa o código diretamente. Use com cuidado e
preferencialmente evite usá-lo em código de
produção.
'''

# Definindo uma string com um laço for e uma condição if
code_str = """
result = []
for i in range(10):
if i % 2 == 0:
result.append(i)
print(result)
"""
# Usando eval para executar a string como código Python
exec(code_str)
