import sqlite3
import pandas as pd


# Conectar ao banco
conn = sqlite3.connect("database/vendas.db")


# 1 - Faturamento total

query = """
SELECT
    SUM(faturamento) AS faturamento_total
FROM vendas;
"""

resultado = pd.read_sql(query, conn)

print("\n💰 Faturamento Total")
print(resultado)



# 2 - Ticket médio

query = """
SELECT
    AVG(faturamento) AS ticket_medio
FROM vendas;
"""

resultado = pd.read_sql(query, conn)

print("\n🎯 Ticket Médio")
print(resultado)



# 3 - Total de unidades vendidas

query = """
SELECT
    SUM(quantidade) AS total_unidades
FROM vendas;
"""

resultado = pd.read_sql(query, conn)

print("\n📦 Total de Unidades Vendidas")
print(resultado)



# 4 - Ranking dos estados

query = """
SELECT
    estado,
    SUM(faturamento) AS receita,
    COUNT(*) AS quantidade_vendas
FROM vendas
GROUP BY estado
ORDER BY receita DESC;
"""

resultado = pd.read_sql(query, conn)

print("\n🗺️ Ranking de Estados")
print(resultado)



# 5 - Produtos com melhor desempenho

query = """
SELECT
    produto,
    SUM(quantidade) AS unidades,
    SUM(faturamento) AS receita
FROM vendas
GROUP BY produto
ORDER BY receita DESC;
"""

resultado = pd.read_sql(query, conn)

print("\n🏆 Produtos com Melhor Desempenho")
print(resultado)



conn.close()