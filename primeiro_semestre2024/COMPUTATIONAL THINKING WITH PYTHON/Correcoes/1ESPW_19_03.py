'''v  = int(input("Diga a v: "))
if v <= 100:
    multa = 0
elif v <= 120:
    multa = 0.2*v
elif v <= 150:
    multa = 0.2*120 + 0.3*v
else:
    multa = 0.2*120 + 0.3*150 + 0.4*v
print(f"Sua multa será de R${multa:.2f}")
lados = int(input("Diga a qtd de lados: "))
forma = ''
if lados < 3:
    print("Polígono não identificado")
elif lados == 3:
    forma = "Triângulo"
elif lados == 4:
    forma = "Quadrado"
elif lados == 5:
    forma = "Pentágono"
else:
    print("Polígono não identificado")
if forma:
    medida = int(input("Diga o tamanho do lado: "))
    perimetro = lados*medida
    print(f"Você escolheu o {forma} com perímetro de {perimetro}")

lados = int(input("Diga a qtd de lados: "))
if lados < 3:
    print("Não é um polígono")
elif lados > 5:
    print("Polígono não identificado")
else:
    medida = int(input("Diga o tamanho do lado: "))
    if lados == 3:
        forma = "Triângulo"
    elif lados == 4:
        forma = "Quadrado"
    else:
        forma = "Pentágono"
    perimetro = lados*medida
    print(f"Você escolheu o {forma} com perímetro de {perimetro}")

num = int(input("Diga um número: "))
if num % 2 == 0:
    print(f"{num} é par!!!!")
else:
    print(f"{num} é impar!!!")

tentativas = 1
senha_cadastrada = '1234'
senha = input("Diga sua senha: ")
while senha != senha_cadastrada and tentativas < 3:
    print("Vc é hacker? ")
    senha = input("Diga sua senha: ")
    tentativas += 1
if senha == senha_cadastrada:
    print("Acesso liberado")
else:
    print("Sai hacker")

i = 0
soma = 0
while i < 10:
    i += 1
    soma += i
print(soma)

i = 0
pares = 0
while i < 10:
    num = int(input(f"Diga o {i+1}º número: "))
    if num%2==0:
        pares += 1
    i+=1
print(f"Vc digitou {pares} pares e {i - pares} impares")

resp = input("Diga sim ou não (s/n): ")
while resp != 's' and resp != 'n':
    resp = input("Diga sim ou não (s/n): ")
if resp == 's':
    print("SIIIIM")
else:
    print("NÃAAAO")

resp = input("Diga sim ou não (s/n): ")
while not (resp == 's' or resp == 'n'):
    resp = input("Diga sim ou não (s/n): ")
if resp == 's':
    print("SIIIIM")
else:
    print("NÃAAAO")
'''
pop = 100000
ano = 0
while pop <= 1e9:
    pop*=2
    ano +=1
print(ano)
