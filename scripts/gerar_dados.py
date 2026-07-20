import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Quantidade de vendas
quantidade = 10000

# Produtos
produtos = [
    "Notebook",
    "Celular",
    "Monitor",
    "Cadeira",
    "Mesa",
    "Teclado",
    "Mouse",
    "Fone"
]

categorias = {
    "Notebook": "Eletrônicos",
    "Celular": "Eletrônicos",
    "Monitor": "Eletrônicos",
    "Cadeira": "Casa",
    "Mesa": "Casa",
    "Teclado": "Eletrônicos",
    "Mouse": "Eletrônicos",
    "Fone": "Eletrônicos"
}

estados = [
    "SP",
    "RJ",
    "MG",
    "PR",
    "SC",
    "RS",
    "BA"
]


dados = []

data_inicio = datetime(2023, 1, 1)

for i in range(quantidade):

    produto = random.choice(produtos)

    registro = {
        "data": data_inicio + timedelta(days=random.randint(0, 1095)),
        "cliente_id": random.randint(1000, 5000),
        "produto": produto,
        "categoria": categorias[produto],
        "estado": random.choice(estados),
        "quantidade": random.randint(1, 5),
        "preco": round(random.uniform(50, 5000), 2)
    }

    dados.append(registro)


df = pd.DataFrame(dados)

# Criar faturamento
df["faturamento"] = df["quantidade"] * df["preco"]


# Salvar CSV
df.to_csv("data/vendas.csv", index=False)


print("Dataset criado com sucesso!")
print(df.head())