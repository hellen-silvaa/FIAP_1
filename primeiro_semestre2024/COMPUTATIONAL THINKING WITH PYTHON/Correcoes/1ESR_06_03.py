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

idade = int(input("Diga sua idade: "))
if idade < 18:
   print("Você não pode usar o Zé Delivery")
else:
   print("Bem vindo ao zé delivery")

idoso = input("Você é idoso? ")
gestante = input("Você é gestante? ")
if idoso == 'sim' or gestante == 'sim':
   print("Pode estacionar")

idoso = input("Você é idoso? ")
cartao = input("Você tem o cartão ? ")
if idoso == 'sim' and cartao == 'sim':
    print("Pode estacionar")
'''
letra = input("Diga uma letra: ")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"{letra} é uma vogal!")
else:
    print(f"{letra} é consoante!")

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
