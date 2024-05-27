frase = "Hello World!"
primeiro_numero = 1
segundo_numero = 1.5
booleana = True
print(frase)
print(type(frase))
print(primeiro_numero)
print(type(primeiro_numero))
print(segundo_numero)
print(type(segundo_numero))
print(booleana)
print(type(booleana))

nome = input("Qual é o seu nome?")
print(f"{nome}, seja bem vinda")

primeiro_numero = int( input({nome} " Diga um numero:"))

segundo_numero = int( input( {nome} "Diga outro numero:"))
soma = primeiro_numero + segundo_numero

print(f" {nome}, A soma entre {primeiro_numero} e {segundo_numero} é {soma}")

soma = primeiro_numero + segundo_numero
print(f"A soma entre {primeiro_numero} e {segundo_numero} é {soma}")

primeiro_numero = 2
segundo_numero = 3
subtracao = primeiro_numero - segundo_numero
print(f"A subtração entre {primeiro_numero} e {segundo_numero} é {subtracao}")

primeiro_numero = 2
segundo_numero = 3
multiplicacao = primeiro_numero * segundo_numero
print(f"A multiplicação entre {primeiro_numero} e {segundo_numero} é {multiplicacao}")

primeiro_numero = 2
segundo_numero = 3
divisao = primeiro_numero / segundo_numero
print(f"A divisão entre {primeiro_numero} e {segundo_numero} é {divisao}")


//sobrescreve a ultima variavel
frase = "Hello"
frase = frase + " World "

print(frase)

nome = input("Diga seu nome: ")
frase = " Eu "
print(frase)
frase = " nome "
frase = " é"

frase = frase + nome
print(f" {frase} ")
print(frase)

aux utilizamos para guardar o a //da para trocar listagens ordenadas

a = 3
b = 5
aux = a

a = b
b = aux
print(a)
print(b)

operadores booleanos >; <; =>; <=; ==(comparador); and, or, in, is, not
a = 2==3
b = 2!=3
c = not 5==6
d= 'h' not in 'hellen'
e= 2>3 or 5!=6
f= 2==3 and 2<3
g= False and True

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
'''



'''OUTRA FORMA DE FAZER'''
'''
frase = "Hello World!"
primeiro_numero = 1
segundo_numero = 1.5
booleana = False
print(frase)
print(type(frase))
print(primeiro_numero)
print(type(primeiro_numero))
print(segundo_numero)
print(type(segundo_numero))
print(booleana)
print(type(booleana))

nome = input("Diga seu seu nome : ")
print(f"Seja bem vindo, {nome}")
primeiro_numero = int(input(f"{nome}, diga um numero : "))
#print(type(primeiro_numero))
segundo_numero = int(input(f"{nome}, diga outro numero : "))
#print(type(segundo_numero))
soma = primeiro_numero + segundo_numero
print(f"A soma entre {primeiro_numero} e {segundo_numero} é {soma}")
sub = primeiro_numero - segundo_numero
print(f"A sub entre {primeiro_numero} e {segundo_numero} é {sub}")
mult = primeiro_numero * segundo_numero
print(f"A multiplicação entre {primeiro_numero} e {segundo_numero} é {mult}")
div = primeiro_numero / segundo_numero
print(f"A divisão entre {primeiro_numero} e {segundo_numero} é {div}")
nome = input("Diga seu nome : ")
frase = "Eu"
print(frase)
frase  = frase + " me"
print(frase)
frase  = frase + " chamo "
print(frase)
frase  = frase + nome
print(frase)

a = 3
b = 5
aux = a
a = b
b = aux
print(a)
print(b)
'''
a = 2==3
b = 2!=3
c = not 5==6
d = 'h' not in 'hellen'
e = 2>3 or 5!=6
f = 2 == 3 and 2<3
g = False and True
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)