'''
#soma multiplicando com laço ele passa 5 vezes no 2 somando
A = 2
B = 5 #multiplicador ->sabemos pelo B quantas vezes irá somar

resultado = 0
for i in range (B):
    resultado += A

print(resultado)'''

#------------------------------------------------------------------------------------

'''A = 2
B = 5

def multiplicacao(A,B):
    if B == 0:
        return 0
    if B == 1:
        return A

    return A + multiplicacao(A, B - 1)

print(multiplicacao(20,6))'''

#a / b divisao conjunto de subtraçoes
'''
def divisao(dividendo, divisor):
    if B == 0:
        return 0
    if B == 1:
        return A

    return A /  divisao( A, B - 1 )

print(divisao(20,5))'''

#------------------------------------------------------------------------------------

#dado um numero qualquer faça uma função recursiva que retorna a soma dos digitos, nao pode lista ne mstring



def somaDigitos (digito):
    if digito < 10:
        return digito
    return digito % 10 + somaDigitos (digito // 10)

print(somaDigitos(1010))

#------------------------------------------------------------------------------------


