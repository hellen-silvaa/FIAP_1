'''#exercício 8
lados = int(input("Diga o número de lados: "))
forma = ''
if lados < 3:
    print("Não é um polígono")
elif lados == 3:
    forma = "Triângulo"
elif lados == 4:
    forma = "Quadrado"
elif lados == 5:
    forma = "Pentágono"
else:
    print("Polígono não identificado")
if forma:
    medida = int(input("Diga a medida do lado: "))
    perimetro = lados*medida
    print(f"O seu polígono é um {forma} e seu perímetro é {perimetro}")


#exercício 8
lados = int(input("Diga o número de lados: "))
if lados < 3:
    print("Não é um polígono")
elif lados > 5:
    print("Polígono não identificado")
else:
    if lados == 3:
        forma = "Triângulo"
    elif lados == 4:
        forma = "Quadrado"
    else:
        forma = "Pentágono"
    medida = int(input("Diga a medida do lado: "))
    perimetro = lados*medida
    print(f"O seu polígono é um {forma} e seu perímetro é {perimetro}")


v = int(input("Diga a velocidade: "))
if v <= 100:
    multa = 0
elif v <= 120:
    multa = 0.2*v
elif v <= 150:
    multa = 0.2*120 + 0.3*v
else:
    multa = 0.2*120 + 0.3*150 + 0.4*v
print(f"A multa será de R${multa:.2f}")
'''
par = 0
num = int(input("Diga o numero : "))
if num%2 == 0:
    par  = par + 1
num = int(input("Diga o numero : "))
if num%2 == 0:
    par  = par + 1
num = int(input("Diga o numero : "))
if num%2 == 0:
    par  = par + 1
num = int(input("Diga o numero : "))
if num%2 == 0:
    par  = par + 1
num = int(input("Diga o numero : "))
if num%2 == 0:
    par  = par + 1
print(f"Vc digitou {par} pares e {5 - par} impares")
