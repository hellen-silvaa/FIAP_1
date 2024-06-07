# Comparações utilizando os operadores de comparação (> , ==, >=, <=, !=)

'''primeiro_numero = 2
segundo_numero = 3
a = primeiro_numero > segundo_numero
print(f"A comparação {primeiro_numero}>{segundo_numero} dá {a}")
a = primeiro_numero == segundo_numero
print(f"A comparação {primeiro_numero}=={segundo_numero} dá {a}")
a = primeiro_numero >= segundo_numero
print(f"A comparação {primeiro_numero}>={segundo_numero} dá {a}")
a = primeiro_numero <= segundo_numero
print(f"A comparação {primeiro_numero}<={segundo_numero} dá {a}")
a = primeiro_numero != segundo_numero
print(f"A comparação {primeiro_numero}!={segundo_numero} dá {a}")


# Comparações e operadores lógicos (or, and, not)

a = 2
b = 3
c = 4
d = 5
print(f"A comparação {a}>{b} or {c}>{d}, ou seja,"
      f" {a>b} or {c>d} dá {a>b or c>d}")
print(f"A comparação {a}!={b} or {c}>{d}, ou seja,"
      f" {a!=b} or {c>d} dá {a!=b or c>d}")
print(f"A comparação {a}>{b} or {c}<{d}, ou seja,"
      f" {a>b} or {c<d} dá {a>b or c<d}")
print(f"A comparação {a}<{b} or {c}<{d}, ou seja,"
      f" {a<b} or {c<d} dá {a<b or c<d}")
print()
print(f"A comparação {a}>{b} and {c}>{d}, ou seja,"
      f" {a>b} and {c>d} dá {a>b and c>d}")
print(f"A comparação {a}!={b} and {c}>{d}, ou seja,"
      f" {a!=b} and {c>d} dá {a!=b and c>d}")
print(f"A comparação {a}>{b} and {c}<{d}, ou seja,"
      f" {a>b} and {c<d} dá {a>b and c<d}")
print(f"A comparação {a}<{b} and {c}<{d}, ou seja,"
      f" {a<b} and {c<d} dá {a<b and c<d}")


# Verifica se a idade é menor que 18 para determinar a permissão de uso do Zé Delivery

idade = int(input("Diga sua idade: "))
if idade < 18:
   print("Você não pode usar o Zé Delivery")
else:
   print("Bem vindo ao zé delivery")


# Verifica se a pessoa é idosa ou gestante para liberar o estacionamento

idoso = input("Você é idoso? ")
gestante = input("Você é gestante? ")
if idoso == 'sim' or gestante == 'sim':
   print("Pode estacionar")


# Verifica se a pessoa é idosa e tem o cartão para liberar o estacionamento

idoso = input("Você é idoso? ")
cartao = input("Você tem o cartão ? ")
if idoso == 'sim' and cartao == 'sim':
    print("Pode estacionar")
'''


# Verifica se a letra é uma vogal ou consoante usando uma condição composta

letra = input("Diga uma letra: ")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"{letra} é uma vogal!")
else:
    print(f"{letra} é consoante!")


# Verifica individualmente cada vogal e atualiza a variável "vogal" para evitar repetição de código


vogal = False
if letra == 'a':
    print(f"{letra} é uma vogal!")
    vogal = True
if letra == 'e':
    print(f"{letra} é uma vogal!")
    vogal = True
if letra == 'i':
    print(f"{letra} é uma vogal!")
    vogal = True
if letra == 'o':
    print(f"{letra} é uma vogal!")
    vogal = True
if letra == 'u':
    print(f"{letra} é uma vogal!")
    vogal = True
if not vogal:
    print(f"{letra} é consoante")


#condicional excludente (quando não ser um, garante ser outro)
'''letra = input("Diga uma letra: ")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"{letra} é uma vogal")
else:
    print(f"{letra} é uma consoante")


nota = int(input("Diga sua nota: "))
if nota >= 6:
    print("Aprovado")
elif nota>=4:
    print("Exame")
else:
    print("Reprovado")


#calculo do imposto de renda com base na tabela

salario = int(input("Diga seu salario: "))
if salario<1903.98:
    aliquota = 0
elif salario < 2826.65:
    aliquota = 0.075
elif salario < 3751.05:
    aliquota = 0.15
elif salario < 4664.68:
    aliquota = 0.225
else:
    aliquota = 0.275
desconto = salario*aliquota
salario = salario - desconto
print(f"O seu salário após descnto de {desconto} será {salario:.2f}")
'''
