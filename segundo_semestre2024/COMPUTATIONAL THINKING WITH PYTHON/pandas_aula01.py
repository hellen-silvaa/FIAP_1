'''Pandas
Pandas é uma biblioteca para Ciência de Dados de código
aberto (open source), construída sobre a linguagem Python, e
que providencia uma abordagem rápida e flexível, com
estruturas robustas para se trabalhar com dados relacionais
(ou rotulados), e tudo isso de maneira simples e intuitiva.
'''
#--------------------------------------------------------------------------------

'''import pandas as pd
# URL do conjunto de dados Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# Nomes das colunas
colunas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
# Carregar os dados diretamente da URL para um DataFrame(DF)
df = pd.read_csv(url, names=colunas)
# Exibindo as primeiras 5 linhas
print(df.head())
print(df)'''

#--------------------------------------------------------------------------------
#mostrando uma serie especifica
'''print(df[['species']])

#mostrando cada elemento de uma serie
for specie in df['species']:
    print(specie)'''
#-------------------------------------------------------------------------
'''import pandas as pd
# URL do conjunto de dados Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# Definindo os nomes das colunas
colunas = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
# Carregando o conjunto de dados
df = pd.read_csv(url, names=colunas)
# Iterando sobre cada linha do DataFrame e imprimindo todas as colunas
for index, row in df.iterrows():
    print(f"Linha {index}: {row['SepalLengthCm']}, {row['SepalWidthCm']},{row['PetalLengthCm']}, {row['PetalWidthCm']}, {row['Species']}")
'''
#------------------------------------------------------------------------------------------------

'''import pandas as pd
# Leitura da planilha (sheet) específica de um arquivo Excel
df = pd.read_excel('vendas_exemplo.xlsx', sheet_name= 'Vendas')
# Exibe as 5 primeiras linhas da planilha
print(df.head())
'''

'''import pandas as pd
# Lê todas as planilhas do arquivo
sheets = pd.read_excel('vendas_exemplo.xlsx', sheet_name=None)
for sheet in sheets:
    print(sheet)'''

#------------------------------------------------------------------------------------------------

'''import pandas as pd
# Lê todas as planilhas do arquivo
sheets = pd.read_excel('vendas_exemplo.xlsx', sheet_name=None)
print('-' * 100)
# Acessa uma planilha pelo nome
df_sheet1 = sheets['Vendas']
print(df_sheet1.head())
def_sheet2 = sheets['Preços dos Produtos']
print('-' * 100)
print(def_sheet2.head())
print('-' * 100)
'''
#------------------------------------------------------------------------------------------------

'''import pandas as pd
dados = {
    'Produto': ['Notebook', 'Teclado', 'Mouse', 'Monitor', 'Impressora'],
    'Quantidade': [12, 100, 75, 20, 15],
    'Preço Unitário (R$)': [3700, 150, 70, 800, 450],
    'Data da Venda': ['2024-01-10', '2024-02-05', '2024-02-20', '2024-03-15', '2024-04-10'],
    'Vendedor': ['Carlos', 'Fernanda', 'Mariana', 'João', 'Ana']
}
# Criando o DataFrame
df_vendas = pd.DataFrame(dados)
# Salvando o DataFrame em um arquivo Excel com múltiplas planilhas
file_path = 'vendas_exemplo_3.xlsx'
# Escrevendo no arquivo Excel
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    df_vendas.to_excel(writer, sheet_name='Sheet1', index=True)
print(f"Arquivo salvo em: {file_path}")'''

#------------------------------------------------------------------------------------------------
#nao sobreescreve os dados ele faz o append na sequencai
'''import pandas as pd
# Caminho do arquivo Excel
file_path = 'vendas_exemplo.xlsx'
# Passo 1: Ler os dados existentes da planilha "Vendas"
df_vendas_existente = pd.read_excel(file_path, sheet_name='Sheet1')
# Passo 2: Criar novos dados que serão adicionados como novas linhas (append)
novos_dados = {
    'Produto': ['Cadeira Gamer', 'Mesa Escritório', 'Smartphone', 'Tablet', 'Headset'],
    'Quantidade': [30, 12, 40, 25, 60],
    'Preço Unitário (R$)': [850, 500, 1200, 700, 200],
    'Data da Venda': ['2024-05-15', '2024-06-01', '2024-06-10', '2024-07-01', '2024-07-15'],
    'Vendedor': ['Lucas', 'Gabriela', 'Fernando', 'Julia', 'Pedro']
}
# Criar um DataFrame com os novos dados
df_novos_dados = pd.DataFrame(novos_dados)
# Passo 3: Concatenar (fazer append) os novos dados nas linhas do DataFrame existente
df_vendas_atualizado = pd.concat([df_vendas_existente, df_novos_dados], ignore_index=True)
# Passo 4: Sobrescrever a planilha "Vendas" com os dados atualizados (mantendo outras planilhas intactas)
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df_vendas_atualizado.to_excel(writer, sheet_name='Vendas', index=False)
print(f"Novas linhas adicionadas ao arquivo {file_path} com sucesso!")'''

#----------------------------------------------------------------------------

#filtrando dados
'''import pandas as pd
# Caminho do arquivo Excel
file_path = 'vendas_exemplo.xlsx'
# Passo 1: Ler os dados existentes da planilha "Vendas"
df_vendas_existente = pd.read_excel(file_path, sheet_name='Vendas')
# Selecionando uma coluna específica
subset = df_vendas_existente[['Produto', 'Quantidade']]
quantidade = df_vendas_existente['Quantidade']
# Filtrando linhas onde o valor na Coluna_A é maior que 50
filtrado = subset[quantidade > 50]
print(filtrado)'''

#----------------------------------------------------------------------------

'''# Modificando valores em uma coluna
df[Quantidade] = df[Quantidade] * 2 # Multiplicando os valores da coluna por 2
# Adicionando uma nova coluna
df['Nova_Coluna'] = df['Coluna_A'] + df['Coluna_B']'''

#----------------------------------------------------------------------------

'''Agrupando Dados e Resumindo Informações
pandas permite agrupar dados com base em uma ou mais colunas e
aplicar funções de agregação como soma, média, contagem, etc.'''
'''import pandas as pd
# Caminho do arquivo Excel
file_path = 'vendas_exemplo.xlsx'
# Passo 1: Ler os dados existentes da planilha "Vendas"
df_vendas_existente = pd.read_excel(file_path, sheet_name='Vendas')
# Agrupando por 'Coluna_A' e calculando a soma de 'Coluna_B' para cada grupo
agrupado = df_vendas_existente.groupby('Produto')['Quantidade'].sum()
# Exibe os resultados
print(agrupado)'''

#----------------------------------------------------------------------------

import pandas as pd
# Caminho do arquivo Excel
file_path = 'vendas_exemplo.xlsx'
# Passo 1: Ler os dados existentes da planilha "Vendas"
df_vendas_existente = pd.read_excel(file_path, sheet_name='Vendas')
# Ordenando por 'Coluna_A' em ordem crescente
df_vendas_existente.sort_values(by='Quantidade', inplace=True)
#df_vendas_existente.sort_values(by='Quantidade',ascending=False, inplace=True)
print(df_vendas_existente)

#----------------------------------------------------------------------------

import pandas as pd
# Definindo uma função personalizada
def aumentar_preco(valor):
    return valor * 1.1 # Aumenta o valor em 10%
# Caminho do arquivo Excel
file_path = 'vendas_exemplo.xlsx'
# Passo 1: Ler os dados existentes da planilha "Vendas"
df_vendas_existente = pd.read_excel(file_path, sheet_name='Vendas')
# Aplicando a função à coluna 'preço'
df_vendas_existente['Preco_Ajustado'] = df_vendas_existente['Preço Unitário (R$)'].apply(aumentar_preco)
subset = df_vendas_existente[['Preço Unitário (R$)', 'Preco_Ajustado']]
print(subset)

#----------------------------------------------------------------------------


df_vendas_existente.to_csv('arquivo.csv', index=False)
df_vendas_existente.to_json('arquivo.json', orient='records')
