#Olá professor, tenha piedade, depois da última prova eu venho estudando python tododia

print('Seja bem vindo à nossa vinheria')
endereco = input('Diga o seu endereço: ')
ano = input('Digite o ano em que você nasceu: ')
while not ano.isnumeric():
    ano = input('O ano em que você nasceu precisa ser número, tente novamente:  ')
ano = int(ano)

if 2024 - ano < 18:
    print('Você é menor de idade, não pode tomar vinho!')
else:
    valor = 0
    qtd_boi = 0
    qtd_tinto = 0
    qtd_marindro = 0
    frete = 10
    while True:
        opcao = input('Qual vinho você deseja comprar? \nboi \ntinto \nmarindro \n')
        while not (opcao == 'boi' or opcao == 'tinto' or opcao == 'marindro'):
            opcao = input('Escolha o vinho que tem no estoque ( boi, tinto ou marindro)')

        qtd = input(f'Quantas garrafas de {opcao} você quer comprar:')
        while not qtd.isnumeric():
            qtd = input(f'A quantidade de garrafas de  tem que ser em número, digite novamente: ')
        qtd = int(qtd)

        if opcao == 'boi':
            valor += 15 * qtd
            qtd_boi += qtd
        elif opcao == 'tinto':
            valor += 25 * qtd
            qtd_tinto += qtd
        else:
            valor += 55 * qtd
            qtd_marindro += qtd
        continuaCompra = input('Você quer continuar comprando mais vinhos? (s/n)')
        while not (continuaCompra == 's' or continuaCompra == 'n'):
            continuaCompra = input('Você quer continaur comprando mais vinhos? (s/n)')
        if continuaCompra == 's':
            continue
        else:
            break
    if valor > 500:
        print('Parabéns você ganhou frete grátis, Volte sempre')
    else:
        valor += 10
print(f'Obrigado você gastou R$ {valor} em {qtd_boi} boi,  {qtd_tinto} e  {qtd_marindro} marindro e os vinhos serão entregue no endereço {endereco}')



