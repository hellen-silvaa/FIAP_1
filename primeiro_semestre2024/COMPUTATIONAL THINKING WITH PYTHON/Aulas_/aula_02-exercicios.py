# 1. Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles

ler_valor1 = int(input("Digite um valor inteiro: "))

ler_valor2 = int(input("Digite outro valor inteiro: "))
if ler_valor1 > ler_valor2:
     print(f"O maior valor é {ler_valor1}")
else:
     print(f"O maior valor é {ler_valor2}")

############################################################
primeiro_numero = int(input("Diga o primeiro número: "))
segundo_numero = int(input("Diga o segundo número: "))
if primeiro_numero > segundo_numero:
    print(primeiro_numero)
else:
    print(segundo_numero)
############################################################

'''****************************************************************************************************************************************************************'''

# 2.Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não
# votar este ano (não é necessário considerar o mês que ela nasceu)

'''ano = int(input("Diga o ano que você nasceu: "))
if ano > 2006 :
   print("Você ainda não pode votar este ano")
else:
   print("Parabéns, você já pode votar este ano!")'''


############################################################
ano = int(input("Diga seu ano de nascimento: "))
idade = 2024 - ano
if idade >= 18:
    print("É obrigatório votar")
elif idade >= 16:
    print("É opcional votar")
else:
    print("Não pode votar")

############################################################



'''****************************************************************************************************************************************************************'''

#3. Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser
# impressas as seguintes mensagens:para validar uma senha fornecida pelo usuario. senha válida . deve ser impressas as seguintes
# mensagens ACESSO PERMITIDO caso a senha seja válida; ACESSO NEGADO caso a senha seja inválida

'''senha = int(input("Digite sua senha: ")) 
if senha == 1234 :
   print("ACESSO PERMITIDO")
else:
   print("ACESSO NEGADO")'''

############################################################
#forma1
senha = int(input("Diga sua senha: "))
senha_cadastrada = 1234
print(type(senha_cadastrada))
if senha == senha_cadastrada:
    print("Acesso Liberado")
else:
    print("Acesso Negado")

#forma2
senha = input("Diga sua senha: ")
senha_cadastrada = '1234'
if senha == senha_cadastrada:
    print("Acesso Liberado")
else:
    print("Acesso Negado")

############################################################


'''****************************************************************************************************************************************************************'''

#4. As maças custam R$ 0.30 cada se forem compradaas menos do que uma dúzia, e R$ 0.25 se forem compradas pelo menos doze. Escreva
# um programa que leia o número de maças compradas, calcule e escreva o valor total da compra

'''macas = int(input("Digite quantas maças deseja comprar: "))

valor_menor_duzia = 0.30
valor_pelomenos_duzia = 0.25

if macas <12:
   valor_total = macas * valor_menor_duzia

else:
   valor_total = macas * valor_pelomenos_duzia

print(f"O valor total da compra é R$ {valor_total:.2f}")'''

'''.2f mostra duas casas decimais após a vírgula'''

############################################################
qtd = int(input("Qts maçãs? "))
preco = 0.3
if qtd >= 12:
    preco = 0.25
print(f"Você pagará R${qtd*preco:.2f}")

############################################################

'''****************************************************************************************************************************************************************'''

#5. Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

'''valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))

if valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
      print("Os valores não podem ser iguais. Por favor, insira valores diferentes.")

elif valor1 < valor2 < valor3:
   menor, meio, maior = valor1, valor2, valor3
elif valor1 < valor3 < valor2:
   menor, meio, maior = valor1, valor3, valor2
elif valor2 < valor1 < valor3:
   menor, meio, maior = valor2, valor1, valor3
elif valor2 < valor3 < valor1:
   menor, meio, maior = valor2, valor3, valor1
elif valor3 < valor2 < valor1:
   menor, meio, maior = valor3, valor2, valor1
else:
   menor, meio, maior = valor3, valor1, valor2

print(f"Os valores em ordem crescente são: {menor}, {meio} e {maior}")'''

#aux guarda o valor da variavel antes de realizar a troca

a = int(input("Diga um número: "))
b = int(input("Diga outro número: "))
c = int(input("Diga outro número: "))

if a > b and a >c :
    aux = a
    a = c
    c = aux

elif b > c
    print(a)
elif b >c :
     print(b)
else:
     print(c)


############################################################

a = int(input("Diga um numero: "))
b = int(input("Diga outro numero: "))
c = int(input("Diga outro numero: "))

if a > b and a > c:
    aux = a
    a = c
    c = aux
elif b > c:
    aux = b
    b = c
    c = aux
if a>b:
    aux = a
    a = b
    b = aux
print(a,b,c)

maior = a
if b>maior:
    maior = b
if c>maior:
    maior = c

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

meio = a + b + c - menor - maior
print(menor,meio,maior)

############################################################


'''****************************************************************************************************************************************************************'''

#6. Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1. feminino 2. masculino) de uma pessoa, construa um programa
# que calcule e imprima seu peso ideal, utilizando as seguintes fórmulas:
#- para homens: (72.7*Altura) -58 -para mulheres; (62.1*Altura)-44.7

'''altura = float(input("Digite sua altura: "))
sexo = int(input(" "Digite o seu sexo (1. feminino 2. masculino):))

if sexo == 1:
 peso_ideal = (62.1 * altura) - 44.7
elif sexo == 2:
 peso_ideal = (72.7 * altura) - 58
else:
 print("Opção inválida, digite 1 para feminino ou 2 para masculino ")

print(f"O peso ideal para a altura de {altura:.2f} metros é aproximadamente {peso_ideal:.2f} kg.")'''

############################################################

sx = int(input("Digite o número correspondente: 1-feminino, 2-masculino"))
altura = float(input("Diga sua altura: "))
peso = 72.7*altura - 58
if sx == 1:
    peso = 62.1*altura - 44.7
print(f"Seu peso ideal é {peso}kg")

############################################################

'''****************************************************************************************************************************************************************'''

#7. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte:
#- Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
#- Se o número de lados for igual a 4 escrever QUADRADO e o valor da área
# Se o número de lados for igual a 5 escrever PENTÁGONO

'''n_lados = int(input("Digite o número de lados do polígono regular: "))
valor = int(input("Digite a medida do lado (em cm): "))

if n_lados == 3:
forma = 'triângulo'
 perimetro= 3*valor

elif n_lados == 4:
forma = 'quadrado'
 perimetro= 3*valor


elif n_lados == 5:
forma = 'pentágono'
 perimetro= 5*valor

print(f"Você escolheu um {forma} com perímetro de {perimetro}")


'''

############################################################

lados = int(input("Diga o número de lados: "))
valor = int(input("Diga o tamanho do lado: "))
if lados == 3:
    forma = 'triângulo'
    perimetro = 3*valor
elif lados == 4:
    forma = 'quadrado'
    perimetro = 4*valor
else:
    forma = 'pentágono'
    perimetro = 5*valor
print(f"Você escolheu um {forma} com perímetro de {perimetro}")

############################################################


'''****************************************************************************************************************************************************************'''

#8. Acrescente as seguintes mensagens à solução anterior conforme o caso.
#-Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
#-Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.
'''

n_lados = int(input("Digite o número de lados do polígono regular: "))

forma = ''
if n_lados<3:
    print("Não é um polígono ")
elif nlados >5:
    print("Polígono não identificado")

else:
   valor = int(input("Digite a medida do lado (em cm): "))
elif n_lados == 3:
forma = 'triângulo'
 perimetro= 3*valor

elif n_lados == 4:
forma = 'quadrado'
 perimetro= 3*valor


elif n_lados == 5:
forma = 'pentágono'
 perimetro= 5*valor

print(f"Você escolheu um {forma} com perímetro de {perimetro}")
'''
############################################################

lados = int(input("Diga o número de lados: "))
if lados<3:
    print("Não é um polígono")
elif lados > 5:
    print("Polígono não identificado")
else:
    valor = int(input("Diga o tamanho do lado: "))
    if lados == 3:
        forma = 'triângulo'
    elif lados == 4:
        forma = 'quadrado'
    elif lados == 5:
        forma = 'pentágono'
    perimetro = lados*valor
    print(f"Você escolheu um {forma} com perímetro de {perimetro}")

############################################################

'''****************************************************************************************************************************************************************'''

#9. Escreva um programa para ler 3 valores inteiros e escrever o maior deles. Considere que o usuário não informará valores iguais
#verifico se o pressuposto esta errado e printo, faço isso testando

a = int(input("Diga um número: "))
b = int(input("Diga outro número: "))
c = int(input("Diga outro número: "))

if a > b and a >c :
    print(a)
elif b >c :
     print(b)
else:
     print(c)

     maior = a
    if b>maior:
        maior = b
    if c>maior:
        maior = c
        print(maior)


############################################################

a = int(input("Diga um numero: "))
b = int(input("Diga outro numero: "))
c = int(input("Diga outro numero: "))

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

maior = a
if b>maior:
    maior = b
if c>maior:
    maior = c
print(maior)


############################################################



'''****************************************************************************************************************************************************************'''

#10. Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:
#-Triângulo Equilátero: possui os 3 lados iguais
#-Triângulo Isóscele: possui  2 lados iguais
#-Triângulo Escaleno: possui os 3 lados diferentes


'''lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 == lado3 and lado1 == lado2:
    print("Equilátero")
elif lado2 == lado2 or lado1 == lado3 or lado1 == lado2:
    print("Isóceles")
else:
    print("Escaleno")'''
############################################################

lado1 = int(input("Diga o primeiro lado: "))
lado2 = int(input("Diga o segundo lado: "))
lado3 = int(input("Diga o terceiro lado: "))

if lado1 == lado3 and lado1 == lado2:
    print("Equilátero")
elif lado3 == lado2 or lado1 == lado3 or lado1 == lado2:
    print("Isósceles")
else:
    print("Escaleno")

############################################################

'''****************************************************************************************************************************************************************'''


#11. Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
#Triangulo Retângulo: possui um ângulo reto (igual a 90º)
#Triangulo Obtusângulo: possui um ângulo obtuso (maior que 90º)
#Triangulo Acutângulo: possui três ângulos agudos (menor que 90º)

'''if ang3+ ang2 + ang1 ==180:
if ang1 == 90 or  ang2 == 90 or ang3 ==90:
    print("Retângulo")
    
elif ang1 > 90 or ang2 >90 or ang3 >90:
    print("Obtuso")
else:
    print("Agudo")
    
else:
    print("Você não manja triângulos ")'''
############################################################

ang1 = int(input("Diga o primeiro angulo: "))
ang2 = int(input("Diga o segundo angulo: "))
ang3 = int(input("Diga o terceiro angulo: "))
if ang3 + ang2 + ang1 == 180:
    if ang1 == 90 or ang2 == 90 or ang3 == 90:
        print("Retângulo")
    elif ang1 > 90 or ang2 > 90 or ang3 > 90:
        print("Obtuso")
    else:
        print("Agudo")
else:
    print("Vc nao manja triangulos")

############################################################
