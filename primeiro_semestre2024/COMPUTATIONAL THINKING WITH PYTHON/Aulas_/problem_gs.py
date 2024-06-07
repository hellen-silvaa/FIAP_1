# Importando as dependências
import matplotlib.pyplot as plt
import numpy as np
 
# Dados que obtivemos ao logo do tempo
anos_atual = np.array([0, 1, 2, 3])
num_animais = np.array([1190, 1155, 1030, 1015])
 
# Ajuste da curva para a função quadrática
coeficiente = np.polyfit(anos_atual, num_animais, 2)
 
# Função quadrática
def f_quadratica(t):
    return coeficiente[0] * t ** 2 + coeficiente[1] * t + coeficiente[2]
 
# Colocando dados no gráfico da previsão da curva
def grafico_dos_dados(f_quadratica, anos, num_animais):
    
    anos = np.linspace(0, 15, 100)
    animais = f_quadratica(anos)

    # Calculando o 5° ano
    ano_5 = f_quadratica(5)

    # Exibindo o gráfico
    plt.figure(figsize=(16,9))
    plt.plot(anos, animais, label = 'N(t)')
    
    # Exibindo pontos atuais
    plt.scatter(anos_atual, num_animais, color = "blue", label = "Dados informados")

    # Exibindo 5° ano
    plt.scatter(5, ano_5, color='red', label='5° ano')

    # Exibindo menor quantidade de elementos
    plt.scatter(8, 880, color='purple', label='Menor número de animais')

    # Legendas do gráfico
    plt.title('Previsão dos animais')
    plt.xlabel("Anos")
    plt.ylabel("Números de animais")
    plt.legend()
    plt.grid(True)
    plt.show()
 
print(f"1a ) Coeficiente: a = {coeficiente[0]:.2f}, b = {coeficiente[1]:.2f}, c = {coeficiente[2]:.2f}\n N(t) = {coeficiente[0]:.2f}t² + {coeficiente[1]:.2f}t + {coeficiente[2]:.2f} " )
print(f"1b ) Estimativas de animais para o 5º ano : {f_quadratica(5):.2f}")
print(f"1c ) Não há nenhum ano em que a população chegará a 0, pois em certo momento ela tende a aumentar.")
print(f"1d ) O menor número de individuos vai ser 880 animais.")
print(f"1e ) Não é possivél calcular o tamanho máximo desta população, pois conforme o gráfico a curva sempre irá aumentar a partir do 8° ano.")

 
grafico_dos_dados(f_quadratica, anos, num_animais)


import matplotlib.pyplot as plt
import numpy as np

# Dados que obtivemos ao logo do tempo
anos_atual = np.array([0, 1, 2, 3])
num_animais = np.array([1190, 1155, 1030, 1015])
 
# Ajuste da curva para a função quadrática
coeficiente = np.polyfit(anos_atual, num_animais, 2)
 
# Função quadrática
def juros_compostos():
    meses = 0
    terabyte = []
    while meses < 100:
        meses += 1
        x = 10 * (1 + 0.03) ** meses
        terabyte.append(x)
        if x > 50:
            break
        
    return terabyte
 
# Colocando dados no gráfico da previsão da curva
def grafico_dos_dados(anos, num_animais):

    meses = []
    terabyte = juros_compostos()

    for i in range(len(terabyte)):
        meses.append(i + 1)

    print(f'2a ) Em um ano de uso teremos: {14.257608868461793:.2f} de terabytes ocupados')
    print(f'2b ) O limite máximo para o uso de 50 terabytes é de {meses[len(meses) - 1]} meses')
    
    # Exibindo o gráfico
    plt.figure(figsize=(16,9))
    plt.plot(meses, terabyte, label = 'Curva de armazenamento')
    plt.scatter( len(meses), terabyte[len(terabyte) - 1] , color='purple', label='Limite de armazenamento')
    plt.scatter( 12, 14.257608868461793 , color='blue', label='1 ano de uso')

    # Legendas do gráfico
    plt.title('Previsão da quantidade de terabyte')
    plt.xlabel("Meses")
    plt.ylabel("Terbytes")
    plt.legend()
    plt.grid(True)
    plt.show()

grafico_dos_dados(anos, num_animais)

import matplotlib.pyplot as plt
import numpy as np

# Dados que obtivemos ao logo do tempo
valor = np.array([50, 55])
quantidade = np.array([800, 780])

coeficiente = np.polyfit(valor, quantidade, 1)
 
def funcao_linear(x):
    return coeficiente[0]*x + coeficiente[1]
 
# Colocando dados no gráfico da previsão da curva
def grafico_dos_dados(func, valor_esperado, quantidade_esperada):

    valor_esperado = np.linspace(50, 115, 50)
    quantidade_esperada = func(valor_esperado)
    valor_50000 = 0
    vendas_50000 = 0
    
    for i in range(len(valor_esperado)):
        receita = valor_esperado[i] * quantidade_esperada[i]
        if receita > 50000:
            valor_50000 = valor_esperado[i]
            vendas_50000 = quantidade_esperada[i]
            break

    print(f'3a ) A relação entre a quantidade e o valor é: {coeficiente[0]:.2f} x + {coeficiente[1]:.2f}')
    print(f'3b ) Ao colocar o preço em R$115,00 a quantidade cai para {quantidade_esperada[len(quantidade_esperada) - 1]:.2f}')
    print(f'3c ) Para obter uma reda de R$50.000,00 é necessário vender a um preço de R${valor_50000:.2f} e uma quantidade de {vendas_50000:.2f}')
    
    # Exibindo o gráfico
    plt.figure(figsize=(16,9))
    plt.plot( valor_esperado, quantidade_esperada, label = 'Curva de quantidade')

    plt.scatter(115, quantidade_esperada[len(quantidade_esperada) - 1], color='blue', label='Valor 115,00')
    plt.scatter(valor_50000 ,vendas_50000, color='black', label='R$ 50.000 de receita')

    # Legendas do gráfico
    plt.title('Previsão da quantidade de vendas pelo preço')
    plt.xlabel("Valor")
    plt.ylabel("Quantidade")
    plt.legend()
    plt.grid(True)
    plt.show()

grafico_dos_dados(funcao_linear, valor, quantidade)

import matplotlib.pyplot as plt
import numpy as np

# Dados que obtivemos ao logo do tempo
valor = np.array([50, 55, 60])
quantidade = np.array([800, 780, 760])

coeficiente = np.polyfit(valor, quantidade, 2)

def f_quadratica(t):
    return coeficiente[0] * t ** 2 + coeficiente[1] * t + coeficiente[2]


# Colocando dados no gráfico da previsão da curva
def grafico_dos_dados(func, valor_esperado, quantidade_esperada):

    valor_esperado = np.linspace(50, 200, 50)
    quantidade_esperada = func(valor_esperado)
    receita = []
    maior_receita = 0
    valor_maior = 0
    quantidade_maior = 0
    
    for i in range(len(valor_esperado)):
        preco_receita = valor_esperado[i] * quantidade_esperada[i]
        receita.append(preco_receita) 

    for i in range(len(receita)):
    
        if receita[i] > maior_receita:
            maior_receita = receita[i]
            valor_maior = valor_esperado[i]
            quantidade_maior = quantidade_esperada[i]
        else:
            break

    print(f'3d ) Para obter a receita máxima é preciso escolher R${valor_maior:.2f} dando {maior_receita:.2f} ')
    
    # Exibindo o gráfico
    plt.figure(figsize=(16,9))
    plt.plot( valor_esperado, receita, label = 'Curva de receita')

    plt.scatter(valor_maior, maior_receita, color='green', label='Maior receita possível')

    # Legendas do gráfico
    plt.title('Previsão da maior receita possível')
    plt.xlabel("Valor(R$)")
    plt.ylabel("Receita(R$)")
    plt.legend()
    plt.grid(True)
    plt.show()

grafico_dos_dados(f_quadratica, valor, quantidade)
