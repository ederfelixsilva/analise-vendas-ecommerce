import pandas as pd
import sqlite3


# Caminhos dos arquivos
arquivo_csv = "data/vendas.csv"
arquivo_banco = "database/vendas.db"


# Ler os dados
df = pd.read_csv(arquivo_csv)

print("Dados carregados:")
print(df.head())


# Criar conexão com SQLite
conn = sqlite3.connect(arquivo_banco)


# Criar tabela vendas
df.to_sql(
    "vendas",
    conn,
    if_exists="replace",
    index=False
)


conn.close()


print("\nBanco criado com sucesso!")
print(f"Arquivo criado: {arquivo_banco}")