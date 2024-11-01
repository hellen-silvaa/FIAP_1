#pip install pymongo
from pymongo import MongoClient
# Conectar ao MongoDB (localhost na porta padrão 27017)
client = MongoClient("mongodb://localhost:27017/")
# Selecionar o banco de dados e a coleção
db = client['fiap']
colecao = db['alunos']

'''# Exemplo de documento
documento = {
"nome": "Hellen Silva",
"idade": 21,
"profissao": "Desenvolvedor Senior"
}
# Inserir um único documento
resultado = colecao.insert_one(documento)
print("Documento inserido com o ID:", resultado.inserted_id)
'''
'''
# Inserir múltiplos documentos
documentos = [
{"nome": "Ana", "idade": 25, "profissao": "Engenheira"},
{"nome": "Carlos", "idade": 40, "profissao": "Arquiteto"}
]
resultado = colecao.insert_many(documentos)
print("IDs dos documentos inseridos:", resultado.inserted_ids)'''

'''# Buscar um único documento
documento = colecao.find_one({"nome": "Ana"})
print("Documento encontrado:", documento)

# Buscar múltiplos documentos
documentos = colecao.find({"idade": {"$gt": 20}})
for doc in documentos:
    print(doc)'''

'''
# Atualizar um único documento
resultado = colecao.update_one(
{"nome": "Hellen Silva"}, # Filtro
{"$set": {"idade": 21}} # Atualização
)
print("Número de documentos modificados:", resultado.modified_count)
# Atualizar múltiplos documentos
resultado = colecao.update_many(
{"idade": {"$lt": 30}}, # Filtro
{"$set": {"status": "jovem"}} # Atualização
)
print("Número de documentos modificados:", resultado.modified_count)'''


'''# Remover um único documento
resultado = colecao.delete_one({"nome": "José Roberto"})
print("Número de documentos deletados:", resultado.deleted_count)
# Remover múltiplos documentos
resultado = colecao.delete_many({"idade": {"$lt": 30}})
print("Número de documentos deletados:", resultado.deleted_count)'''

'''# Remover um único documento
resultado = colecao.delete_one({"nome": "Hellen Silva"})
print("Número de documentos deletados:", resultado.deleted_count)
# Remover múltiplos documentos
resultado = colecao.delete_many({"idade": {"$lt": 30}})
print("Número de documentos deletados:", resultado.deleted_count)'''

'''documentos = [
{"nome": "Maria", "idade": 28, "profissao": "Designer"},
{"nome": "Pedro", "idade": 35, "profissao": "Analista"},
{"nome": "Ana", "idade": 22, "profissao": "Estagiária"}
]
resultado = colecao.insert_many(documentos)
print("IDs dos documentos inseridos:", resultado.inserted_ids)'''

'''$gt, $lt: Maior que e menor que
$in: Verifica se um valor está em uma lista'''
'''# Buscar todos com idade maior que 25 e profissão 'Designer' ou 'Analista'
filtro = {
"idade": {"$gt": 25},
"profissao": {"$in": ["Designer", "Analista"]}
}
resultados = colecao.find(filtro)
for doc in resultados:
    print(doc)
'''

'''# Buscar documentos, mas retornar apenas os campos 'nome' e 'idade'
projecao = {"_id": 0, "nome": 1, "idade": 1} # 1 para incluir, 0 para excluir
resultados = colecao.find({}, projection=projecao)
for doc in resultados:
    print(doc)'''

'''# Ordenar por idade (crescente) e depois por nome (decrescente)
resultados = colecao.find().sort([("idade", 1), ("nome", -1)])
for doc in resultados:
    print(doc)'''

'''# Obter apenas os 2 primeiros documentos
resultados = colecao.find().limit(2)
for doc in resultados:
    print(doc)'''


'''Atualizações Parciais com update_one e update_many
Além de update_one e update_many, há operadores de atualização
úteis:
$set: Define um novo valor para um campo
$inc: Incrementa o valor de um campo numérico
$push: Adiciona um item a uma lista
$pull: Remove itens de uma lista'''

'''# Incrementar a idade em 1
colecao.update_one({"nome": "José Roberto"}, {"$inc": {"idade": 1}})
# Adicionar uma nova habilidade em um array de habilidades
colecao.update_one({"nome": "José Roberto"}, {"$push": {"habilidades":
"Python"}})
# Remover uma habilidade específica da lista
colecao.update_one({"nome": "José Roberto"}, {"$pull": {"habilidades":
"Python"}})
'''

'''# Contar quantos documentos têm idade maior que 25
contagem = colecao.count_documents({"idade": {"$gt": 25}})
print("Número de documentos com idade > 25:", contagem)'''

# Agrupar documentos por profissão e contar quantas pessoas em cada profissão
'''pipeline = [
{"$group": {"_id": "$profissao", "contagem": {"$sum": 1}}}
]
resultados = colecao.aggregate(pipeline)
for doc in resultados:
    print(doc)
    '''

'''# Criar um índice no campo 'idade'
colecao.create_index("idade")
# Criar um índice composto em 'nome' e 'profissao'
colecao.create_index([("nome", 1), ("profissao", 1)])'''

'''
Busca por Texto Completo
Se a coleção tiver índices de texto, você pode realizar buscas de texto
completo.'''
# Criar um índice de texto
'''colecao.create_index([("profissao", "text")])
# Realizar busca de texto
resultados = colecao.find({"$text": {"$search": "Desenvolvedor"}})
for doc in resultados:
    print(doc)
'''

'''# Excluir todos os documentos onde idade é menor que 30
resultado = colecao.delete_many({"idade": {"$lt": 30}})
print("Número de documentos deletados:", resultado.deleted_count)'''


# Atualizar idade e retornar o documento atualizado
documento_atualizado = colecao.find_one_and_update(
{"nome": "José Roberto"},
{"$set": {"idade": 35}},
return_document=True # Retorna o documento depois da atualização
)
print(documento_atualizado)
