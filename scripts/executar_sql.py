import sqlite3
import pandas as pd


# Conectar ao banco
conn = sqlite3.connect("database/vendas.db")


# Consulta 1 - Faturamento por produto
query_produto = """
SELECT
    produto,
    SUM(faturamento) AS receita_total
FROM vendas
GROUP BY produto
ORDER BY receita_total DESC;
"""


resultado_produto = pd.read_sql(query_produto, conn)

print("\n🏆 Faturamento por Produto")
print(resultado_produto)


# Consulta 2 - Faturamento por estado
query_estado = """
SELECT
    estado,
    SUM(faturamento) AS receita_estado
FROM vendas
GROUP BY estado
ORDER BY receita_estado DESC;
"""


resultado_estado = pd.read_sql(query_estado, conn)

print("\n🗺️ Faturamento por Estado")
print(resultado_estado)


# Consulta 3 - Produtos mais vendidos
query_quantidade = """
SELECT
    produto,
    SUM(quantidade) AS unidades_vendidas
FROM vendas
GROUP BY produto
ORDER BY unidades_vendidas DESC;
"""


resultado_quantidade = pd.read_sql(query_quantidade, conn)

print("\n📦 Produtos Mais Vendidos")
print(resultado_quantidade)


# Consulta 4 - Evolução mensal
query_mensal = """
SELECT
    strftime('%Y-%m', data) AS mes,
    SUM(faturamento) AS receita_mensal
FROM vendas
GROUP BY mes
ORDER BY mes;
"""


resultado_mensal = pd.read_sql(query_mensal, conn)

print("\n📈 Evolução Mensal")
print(resultado_mensal)


conn.close()