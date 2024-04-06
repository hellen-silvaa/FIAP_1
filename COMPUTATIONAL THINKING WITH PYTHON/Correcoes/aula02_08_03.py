'''letra = input("Diga uma letra: ")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"{letra} é uma vogal")
else:
    print(f"{letra} é uma consoante")
nota = int(input("Diga sua nota: "))
if nota >= 6:
    print("Aprovado")
elif nota<6 and nota>=4:
    print("Exame")
else:
    print("Reprovado")
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
