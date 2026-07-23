<div align="center">

# 📊 Análise de Vendas de E-commerce

### Do dado bruto à decisão de negócio: um projeto de Análise de Dados com Python

Geração, limpeza, exploração e visualização de dados de vendas para transformar números em insights.

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

Este projeto foi desenvolvido para **praticar o ciclo completo de um projeto de Análise de Dados**, utilizando Python como ferramenta principal. A proposta é simular a rotina de um analista de dados dentro de uma operação de e-commerce, percorrendo cada etapa do processo:

<div align="center">

**Dados brutos → Limpeza → Exploração → Visualização → Insights → Decisão**

</div>

### 🎯 Objetivo Principal

Aplicar, na prática, técnicas de manipulação, tratamento e análise exploratória de dados com **Pandas** e **Matplotlib**, produzindo visualizações que ajudem a responder perguntas de negócio relevantes para um e-commerce.

### 💼 Problema de Negócio

Empresas de e-commerce lidam constantemente com grandes volumes de dados de vendas — produtos, valores, datas, localidades — mas nem sempre esses dados são organizados de forma a gerar valor. Este projeto simula esse cenário: a partir de uma base de vendas, busca-se entender **quais produtos e regiões merecem mais atenção comercial** e **como a receita se comporta ao longo do tempo**.

### 💡 Motivação

Como parte da minha formação em Análise e Desenvolvimento de Sistemas, este projeto foi construído para consolidar conhecimentos de Análise de Dados de ponta a ponta — não apenas a parte técnica de código, mas também a capacidade de **interpretar resultados e comunicá-los de forma clara**, como faria um analista de dados em um time real.

### 🔍 Como esse tipo de análise ajuda um e-commerce

Ao organizar e visualizar dados de vendas dessa forma, uma empresa consegue:

- Identificar quais produtos concentram maior parte da receita
- Entender em quais estados/regiões a operação é mais forte
- Acompanhar a evolução do faturamento ao longo do tempo
- Comparar volume de vendas com receita gerada, apoiando decisões de estoque e precificação

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
- 📅 **Manipulação de datas** — conversão e padronização de campos temporais
- 🔎 **Análise exploratória (EDA)** — exploração inicial da base de dados
- 💰 **Cálculo de faturamento** — por produto e por estado
- 🗺️ **Análise regional** — distribuição geográfica das vendas
- 📈 **Análise temporal** — evolução do faturamento ao longo do tempo
- 📊 **Visualizações** — gráficos gerados com Matplotlib
- 💾 **Exportação dos gráficos** — salvamento automático na pasta `images/`

<br/>

---

## 🛠️ Tecnologias

| Tecnologia | Utilização |
|---|---|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | Linguagem principal do projeto |
| ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | Manipulação, limpeza e análise dos dados |
| ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat-square&logo=plotly&logoColor=white) | Criação das visualizações |
| ![Jupyter](https://img.shields.io/badge/-Jupyter%20Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white) | Ambiente interativo para análise |
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

Consolida a receita gerada por cada produto do catálogo, permitindo identificar quais itens têm maior relevância para o faturamento total e apoiando decisões comerciais, como priorização de vitrine e campanhas.

### 🗺️ Faturamento por Estado

Analisa a distribuição geográfica das vendas, ajudando a identificar em quais estados a operação já é forte e onde existem possíveis oportunidades de expansão comercial.

### 📅 Evolução Temporal

Observa o comportamento do faturamento ao longo do tempo, permitindo identificar tendências de crescimento e possíveis padrões sazonais que merecem atenção do time de negócio.

### 📦 Quantidade Vendida por Produto

Analisa o volume de unidades vendidas por produto, trazendo a perspectiva de demanda — informação que, comparada ao faturamento, apoia decisões de estoque e planejamento de compras.

<br/>

---

## 💡 Principais Insights

> Leitura dos resultados no formato de um breve relatório, como seria apresentado a um time de negócio:

- 🏆 **Concentração de receita** — alguns produtos tendem a representar uma parcela maior do faturamento total, o que pode indicar oportunidade de priorização comercial sobre esses itens específicos.
- 🗺️ **Distribuição regional** — diferenças no faturamento entre estados podem sinalizar mercados já consolidados e outros com potencial ainda pouco explorado.
- 📈 **Tendência temporal** — a evolução mensal do faturamento permite observar períodos de crescimento ou retração, informação útil para o planejamento de ações comerciais futuras.
- 📦 **Volume x Receita** — produtos com maior quantidade vendida não necessariamente são os que mais faturam, reforçando a importância de olhar volume e receita em conjunto, e não isoladamente.

<br/>

---

## 🔮 Melhorias Futuras

- [ ] 📊 **Dashboard Power BI** — transformar as análises em um painel interativo
- [ ] 📈 **Dashboard Plotly/Dash** — construir visualizações dinâmicas em Python
- [ ] 🗄️ **SQL e Data Warehouse** — migrar as análises para consultas SQL e uma modelagem dimensional
- [ ] 🤖 **Machine Learning** — aplicar modelos de previsão de vendas (forecasting)
- [ ] ☁️ **Deploy** — publicar o dashboard em um serviço de nuvem
- [ ] 🔄 **Pipeline ETL** — automatizar a atualização e o processamento dos dados
- [ ] 🧪 **Testes automatizados** — adicionar testes para as etapas de tratamento de dados

<br/>

---

## 🎓 Aprendizados

Durante o desenvolvimento deste projeto, os principais pontos de evolução foram:

- Manipulação e transformação de dados com **Pandas**
- Boas práticas de **limpeza e tratamento de dados**
- Condução de uma **análise exploratória (EDA)** de forma estruturada
- Criação de **visualizações** claras e objetivas com Matplotlib
- Desenvolvimento do raciocínio analítico para transformar dados em possíveis decisões de negócio
- Organização de um projeto de dados seguindo **boas práticas de estrutura e documentação**

<br/>

---

## 👨‍💻 Autor

<div align="center">

### Éder Felix Silva

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
