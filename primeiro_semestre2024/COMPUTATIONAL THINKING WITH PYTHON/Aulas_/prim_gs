# Retorna maior local danificado
def maior_Numero(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

# Retorna soma das danificações dos corais
def soma_Lista(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma 

# Retorna index dentro do array
def acha_index(elemento, lista):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i

# Retorna uma lista de quanto foi danificado
def danificacao_Corais(extencoes, porcentagens):
    danificacao = []
    for i in range(len(extencoes)):
        quantidade_danificada = extencoes[i] * (porcentagens[i] / 100)
        danificacao.append(float(f'{quantidade_danificada:.2f}'))
    return danificacao

# Retorna ordem crescente dos locais mais danificados
def ordem_crescente(lista):
    ordem = lista[:]
    for i in range(len(lista)):
        for i in range(len(ordem)):
            if not (i + 1 == len(ordem)) :
                if ordem[i] > ordem[i + 1] :
                    aux = ordem[i]
                    ordem[i] = ordem[i + 1]
                    ordem[i + 1] = aux
    return ordem
    
# Acha os top 3 com maior danificação dos corais
def top_preocupantes(danificacao, locais):
    ordem = ordem_crescente(danificacao)
    lista_preocupantes = [ordem[len(ordem) - 1], ordem[len(ordem) - 2], ordem[len(ordem) - 3]]
    nomes_precupantes = []
    for i in range(len(lista_preocupantes)):
        index = acha_index(lista_preocupantes[i], danificacao)
        nomes_precupantes.append(locais[index])
    return lista_preocupantes, nomes_precupantes


# Força usuario a digitar algo que esta dentro do array
def forca_usuario_digitar(opcoes, mensagem):
    while True:
        escolha = input(mensagem)
        if escolha in opcoes:
            return escolha
        print('Selecione uma opção da lista') 

# Adição de dados 
costa_litoranea = ['Bahia', 'Maranhão', 'Rio de Janeiro', 'Rio Grande do Sul', 'São Paulo', 'Amapá', 'Ceará', 'Pará', 'Santa Catarina', 'Rio Grande do Norte', 'Espirito Santo', 'Alagoas', 'Pernambuco', 'Sergipe', 'Paraíba', 'Paraná', 'Piauí']
extencao_Litoral = [932, 640, 636, 623, 622, 598, 573, 562, 531, 410, 392, 229, 187, 163, 117, 98, 66]
porcentagem_corais_danificados = [10, 13, 8, 8, 4, 6, 6, 4, 7, 6, 3, 9, 8, 3, 8, 4, 5]

danificacao = danificacao_Corais(extencao_Litoral, porcentagem_corais_danificados)
ordemC = ordem_crescente(danificacao)
top3 = top_preocupantes(danificacao, costa_litoranea)

# Interação com o usuario
print("Bem-vindo ao sistema de monitoramento de corais!")
print("O que você quer saber sobre os corais ?\n"
      '1 - Todas as informações\n'
      '2 - Um estados especifo\n'
      '3 - Media de todos os estados')
opcao = forca_usuario_digitar(['1', '2', '3'], 'Selecione 1, 2 ou 3: ')
if opcao == '1':
    print('\nTodas as informações:')
    for i in range(len(costa_litoranea)):
        print(f'{costa_litoranea[i]} de {extencao_Litoral[i]} km,\n{danificacao[i]} /m² danificados\n')
    
    print(f'\nOs 3 estados mais preocupantes são:\n'
            f'1º - {top3[1][0]} com {top3[0][0]} /m²\n'
            f'2º - {top3[1][1]} com {top3[0][1]} /m²\n'
            f'3º - {top3[1][2]} com {top3[0][2]} /m²\n')
elif opcao == '2':
    print(f'Cidades: {costa_litoranea}')
    estado = forca_usuario_digitar(costa_litoranea, 'Selecione um estado: ')
    index = acha_index(estado, costa_litoranea)
    
    print(f'\n{estado} de {extencao_Litoral[index]} km,\n'
          f'{danificacao[index]} /m² danificados\n')
else:
    print(f'- O comprimento do litoral no Brasil é {soma_Lista(extencao_Litoral)} km\n'
          f'- A soma das danificações é {soma_Lista(danificacao)} /m²\n'
          f'- A média das danificações por estado é {(soma_Lista(danificacao) / len(danificacao)):.2f} /m²')
