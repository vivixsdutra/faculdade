from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

# 1- Total de Vendas por dia :

result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$data_compra", "totalVendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"_id": 1}}
])
writeAJson(result, "Total de Vendas por dia")


# 2- Produto mais vendido:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "quantidadeTotal": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"quantidadeTotal": -1}},
    {"$limit": 1}
])
writeAJson(result, "Produto mais vendido")

# 3- Cliente que mais gastou:
result = db.collection.aggregate([
    {"$group": {"_id": "$cliente_id", "gastoMaximo": {"$max": "$preco"}}},
    {"$sort": {"gastoMaximo": -1}},
    {"$limit": 1}
])
writeAJson(result, "Cliente que mais gastou")

# 4- Produtos que venderam mais de 1 unidade:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "quantidadeTotal": {"$sum": "$produtos.quantidade"}}},
    {"$match": {"quantidadeTotal": {"$gt": 1}}},
    {"$sort": {"quantidadeTotal": -1}}
])
writeAJson(result, "Produtos que venderam mais de 1 unidade")
