'''par = 0
qtd = 0
while qtd < 5:
    num = int(input("Diga um número: "))
    if num%2 == 0:
       par += 1
    qtd += 1
print(f"Vc digitou {par} pares e {5-par} impares")

senha_cadastrada = '1234'
senha = input("Diga sua senha: ")
qtd = 1
while senha != senha_cadastrada and qtd < 3:
    print(f"Vc é hacker? Só mais {3 - qtd} tentativas")
    senha = input("Diga sua senha: ")
    qtd += 1
if senha == senha_cadastrada:
    print("Acesso liberado!")
else:
    print("Sai hacker!!!")
'''
i = 0
soma = 0
while i < 100:
    i+=1
    soma += i
print(soma)
