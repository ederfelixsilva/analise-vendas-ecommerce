<div align="center">

# 📊 Análise de Vendas de E-commerce

### Transformando dados de vendas em decisões de negócio

Um projeto de Análise de Dados com Python que percorre o fluxo completo do trabalho de um analista: da geração dos dados à extração de insights.

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

[![GitHub stars](https://img.shields.io/github/stars/ederfelixsilva/analise-vendas-ecommerce?style=flat-square&color=yellow)](#)
[![GitHub last commit](https://img.shields.io/github/last-commit/ederfelixsilva/analise-vendas-ecommerce?style=flat-square)](#)
[![Status](https://img.shields.io/badge/status-concluído-success?style=flat-square)](#)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square)](#)

<br/>

[📖 Sobre](#-sobre-o-projeto) •
[🗂️ Dataset](#️-dataset) •
[🖼️ Demonstração](#️-demonstração) •
[⚙️ Funcionalidades](#️-funcionalidades) •
[🛠️ Tecnologias](#️-tecnologias) •
[🚀 Como Executar](#-como-executar) •
[📈 Análises](#-análises-realizadas) •
[💡 Insights](#-principais-insights) •
[👨‍💻 Autor](#-autor)

</div>

<br/>

---

## 📖 Sobre o Projeto

Este projeto foi desenvolvido para praticar, de ponta a ponta, o ciclo de trabalho de um **Analista de Dados** aplicado a um cenário de e-commerce. A proposta central não é apenas escrever código, mas percorrer o raciocínio completo por trás de uma análise:

<div align="center">

**Dados brutos → Tratamento → Exploração → Visualização → Insights → Decisão**

</div>

### 🎯 Objetivo

Utilizar **Python**, **Pandas** e **Matplotlib** para transformar uma base de vendas em informação útil — identificando padrões de faturamento, comportamento regional e evolução temporal que possam apoiar decisões comerciais.

### 💼 Problema de Negócio

Em uma operação de e-commerce, dados de vendas são gerados constantemente, mas nem sempre chegam de forma organizada até quem precisa decidir. Antes de qualquer decisão comercial — como priorizar um produto, reforçar estoque ou direcionar investimento para uma região — é preciso primeiro **entender o que os dados mostram**. Este projeto simula justamente essa etapa: transformar uma base bruta de vendas em uma leitura clara do negócio.

### 💡 Motivação

Como parte da minha formação em Análise e Desenvolvimento de Sistemas, este projeto foi construído para consolidar a prática de Análise de Dados como um todo — não só a manipulação técnica com Pandas, mas também a capacidade de interpretar os resultados e comunicá-los de forma objetiva, como faria um analista dentro de uma empresa.

### 📌 Por que essa análise importa

- Ajuda a entender **onde está concentrada a receita** do negócio
- Evidencia **diferenças regionais** que podem orientar estratégias comerciais
- Permite acompanhar a **evolução do faturamento** ao longo do tempo
- Compara **volume de vendas com receita gerada**, apoiando decisões de estoque

<br/>

---

## 🗂️ Dataset

O dataset utilizado neste projeto é **sintético**, gerado via script Python (`scripts/gerar_dados.py`), e foi construído para simular uma operação real de e-commerce, contendo informações de vendas por cliente, produto, categoria, estado e período.

| Coluna | Descrição |
|---|---|
| `data` | Data em que a venda foi realizada |
| `cliente_id` | Identificador único do cliente |
| `produto` | Nome do produto vendido |
| `categoria` | Categoria à qual o produto pertence |
| `estado` | Estado (UF) onde a venda foi realizada |
| `quantidade` | Quantidade de unidades vendidas na transação |
| `preco` | Preço unitário do produto |
| `faturamento` | Valor total gerado pela venda (quantidade × preço) |

Essa estrutura permite responder perguntas de negócio como: quais produtos e categorias geram mais receita, como as vendas se distribuem entre os estados, e como o faturamento evolui mês a mês — a base de qualquer análise comercial em um e-commerce.

<br/>

---

## 🖼️ Demonstração

<div align="center">

### 💰 Faturamento por Estado
<img src="images/faturamento_estado.png" alt="Faturamento por Estado" width="700"/>

<br/><br/>

### 📅 Evolução Mensal do Faturamento
<img src="images/faturamento_mensal.png" alt="Faturamento Mensal" width="700"/>

<br/><br/>

### 🏆 Faturamento por Produto
<img src="images/faturamento_produto.png" alt="Faturamento por Produto" width="700"/>

<br/><br/>

### 📦 Quantidade Vendida por Produto
<img src="images/quantidade_produto.png" alt="Quantidade por Produto" width="700"/>

</div>

> 💬 Todas as imagens acima são geradas automaticamente ao executar o notebook e salvas na pasta `images/`.

<br/>

---

## ⚙️ Funcionalidades

- 🧪 **Geração de dados** — criação de um dataset sintético de vendas de e-commerce
- 🧹 **Limpeza e tratamento** — tratamento de valores nulos, duplicados e inconsistências
- 📅 **Conversão de datas** — padronização de campos temporais para análise
- 🔎 **Análise exploratória (EDA)** — exploração inicial e entendimento da base
- 💰 **Faturamento por produto** — cálculo da receita gerada por item
- 🗺️ **Faturamento por estado** — cálculo da receita por região
- 📈 **Evolução temporal** — acompanhamento do faturamento ao longo do tempo
- 📦 **Quantidade vendida por produto** — análise de volume por item
- 💾 **Geração automática de gráficos** — visualizações salvas em `images/`

<br/>

---

## 🛠️ Tecnologias

| Tecnologia | Utilização |
|---|---|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | Linguagem principal do projeto |
| ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | Manipulação, limpeza e análise dos dados |
| ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat-square&logo=plotly&logoColor=white) | Criação das visualizações |
| ![Jupyter](https://img.shields.io/badge/-Jupyter%20Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white) | Ambiente interativo para condução da análise |
| ![Git](https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white) | Controle de versão |
| ![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white) | Hospedagem e documentação do projeto |

<br/>

---

## 📁 Estrutura do Projeto

```
analise-vendas-ecommerce/
│
├── data/
│   └── vendas.csv                    # Dataset de vendas utilizado na análise
│
├── images/
│   ├── faturamento_estado.png        # Gráfico: faturamento por estado
│   ├── faturamento_mensal.png        # Gráfico: evolução mensal do faturamento
│   ├── faturamento_produto.png       # Gráfico: faturamento por produto
│   └── quantidade_produto.png        # Gráfico: quantidade vendida por produto
│
├── notebooks/
│   └── analise_vendas.ipynb          # Notebook principal com toda a análise
│
├── scripts/
│   └── gerar_dados.py                # Script de geração do dataset sintético
│
├── requirements.txt                  # Dependências do projeto
├── README.md                         # Documentação do projeto
└── .gitignore                        # Arquivos e pastas ignorados pelo Git
```

- **`data/`** — armazena o dataset de vendas utilizado nas análises
- **`images/`** — armazena os gráficos gerados automaticamente pelo notebook
- **`notebooks/`** — contém o notebook com todo o processo de análise, documentado passo a passo
- **`scripts/`** — contém o script responsável por gerar o dataset sintético

<br/>

---

## 🚀 Como Executar

### ✅ Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### 1️⃣ Clonar o projeto

```bash
git clone https://github.com/ederfelixsilva/analise-vendas-ecommerce.git
```

### 2️⃣ Entrar na pasta do projeto

```bash
cd analise-vendas-ecommerce
```

### 3️⃣ Criar ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 5️⃣ Gerar o dataset

```bash
python scripts/gerar_dados.py
```

### 6️⃣ Executar a análise

```bash
jupyter notebook notebooks/analise_vendas.ipynb
```

> 💡 Ao executar todas as células do notebook, os gráficos serão gerados e salvos automaticamente na pasta `images/`.

<br/>

---

## 📈 Análises Realizadas

### 💰 Faturamento por Produto

Consolida a receita gerada por cada produto do catálogo, permitindo identificar quais itens têm maior peso no faturamento total — informação relevante para decisões como priorização de vitrine, campanhas e negociação com fornecedores.

### 🗺️ Faturamento por Estado

Analisa a distribuição geográfica das vendas, ajudando a identificar em quais estados a operação já é mais forte e onde podem existir oportunidades de expansão comercial ou ações de marketing regional.

### 📅 Evolução Temporal

Observa o comportamento do faturamento mês a mês, permitindo identificar tendências de crescimento, possíveis quedas e padrões sazonais relevantes para o planejamento comercial.

### 📦 Quantidade Vendida por Produto

Analisa o volume de unidades vendidas por produto, trazendo a perspectiva de demanda. Combinada à análise de faturamento, apoia decisões relacionadas a estoque e planejamento de compras.

<br/>

---

## 💡 Principais Insights

> Leitura dos resultados no formato de uma apresentação executiva, como seria levada a um time de negócio:

- 🏆 **Concentração de receita** — parte do catálogo tende a concentrar a maior fatia do faturamento total, o que reforça a importância de priorizar esses produtos em ações comerciais e de estoque.
- 🗺️ **Diferenças regionais** — o faturamento não se distribui de forma homogênea entre os estados, o que pode indicar tanto mercados já consolidados quanto regiões com potencial de crescimento ainda pouco explorado.
- 📈 **Comportamento temporal** — a evolução mensal do faturamento permite observar se o negócio está em trajetória de crescimento, estabilidade ou retração, e se existem meses que se destacam.
- 📦 **Volume x Receita** — produtos com maior volume de vendas não são necessariamente os que mais faturam, o que reforça a necessidade de olhar quantidade e receita em conjunto, e não isoladamente, ao definir prioridades.

<br/>

---

## 🎯 Resultados da Análise

De forma geral, este projeto demonstra como um conjunto de dados de vendas pode ser transformado em leitura de negócio, permitindo:

- Identificar **padrões de venda** por produto e por período
- Compreender a **distribuição regional** das vendas e onde a operação é mais relevante
- Reconhecer **quais produtos concentram maior impacto** no faturamento
- Fornecer uma base analítica que **apoia a tomada de decisão comercial**, como priorização de produtos, direcionamento regional e planejamento de estoque

<br/>

---

## 🔮 Melhorias Futuras

- [ ] 📊 **Dashboard Power BI** — transformar as análises em um painel interativo
- [ ] 🖥️ **Dashboard Streamlit** — criar uma aplicação web interativa em Python
- [ ] 📈 **Plotly/Dash** — construir visualizações dinâmicas e interativas
- [ ] 🗄️ **SQL** — migrar as análises para consultas SQL
- [ ] 🏛️ **Data Warehouse** — estruturar uma modelagem dimensional para os dados
- [ ] 🤖 **Machine Learning** — aplicar modelos preditivos sobre os dados de vendas
- [ ] 🔮 **Forecasting** — prever tendências futuras de faturamento
- [ ] 🔄 **Pipeline ETL** — automatizar a extração, transformação e carga dos dados
- [ ] ☁️ **Cloud Deploy** — publicar a análise ou dashboard em um serviço de nuvem
- [ ] 🧪 **Testes automatizados** — adicionar testes para as etapas de tratamento de dados

<br/>

---

## 🎓 Aprendizados

Durante o desenvolvimento deste projeto, os principais pontos de evolução foram:

- Aprofundamento em **Python** aplicado à análise de dados
- Manipulação e transformação de dados com **Pandas**
- Boas práticas de **limpeza e tratamento de dados**
- Condução de uma **análise exploratória (EDA)** de forma estruturada
- Criação de **visualizações** claras e objetivas com Matplotlib
- Desenvolvimento do raciocínio analítico necessário para transformar dados em possíveis decisões de negócio
- Fortalecimento da **comunicação de insights** para públicos não técnicos
- Organização de um projeto de dados seguindo **boas práticas profissionais de estrutura e documentação**

<br/>

---

## 👨‍💻 Autor

<div align="center">

### Éder Félix Silva

Estudante de Análise e Desenvolvimento de Sistemas

📊 Análise de Dados &nbsp;•&nbsp; 🐍 Python &nbsp;•&nbsp; 🗄️ SQL &nbsp;•&nbsp; ☁️ Cloud Computing

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eder-f%C3%A9lix/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ederfelixsilva)

</div>

<br/>

---

<div align="center">

**⭐ Se este projeto foi útil ou interessante, considere deixar uma estrela no repositório.**

</div>
