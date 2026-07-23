<div align="center">

# 📊 Análise de Vendas de E-commerce

### Transformando dados brutos em decisões de negócio inteligentes

Um projeto completo de Análise de Dados com Python — da geração e limpeza dos dados até insights acionáveis para o negócio.

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

[![Status](https://img.shields.io/badge/Status-Concluído-success?style=flat-square)](#)
[![GitHub stars](https://img.shields.io/github/stars/ederfelixsilva/analise-vendas-ecommerce?style=flat-square&color=yellow)](#)
[![GitHub last commit](https://img.shields.io/github/last-commit/ederfelixsilva/analise-vendas-ecommerce?style=flat-square)](#)
[![GitHub repo size](https://img.shields.io/github/repo-size/ederfelixsilva/analise-vendas-ecommerce?style=flat-square)](#)

<br/>

[📖 Sobre](#-sobre-o-projeto) •
[🖼️ Demonstração](#️-demonstração) •
[⚙️ Funcionalidades](#️-funcionalidades) •
[🚀 Como Executar](#-como-executar) •
[📈 Análises](#-análises-realizadas) •
[💡 Insights](#-principais-insights) •
[👨‍💻 Autor](#-autor)

</div>

<br/>

---

## 📖 Sobre o Projeto

O **Análise de Vendas de E-commerce** é um projeto end-to-end de Data Analysis construído para simular — do início ao fim — a rotina de um analista de dados dentro de uma operação de e-commerce: desde a **geração de um dataset sintético realista**, passando pela **limpeza e tratamento dos dados**, até a **análise exploratória (EDA)** e a **produção de visualizações** que sustentam decisões de negócio.

Mais do que um exercício técnico, o projeto foi desenhado para responder perguntas reais que qualquer time comercial ou de produto faria:

> *Quais produtos mais vendem? Quais estados geram mais receita? As vendas estão crescendo ao longo do tempo? Onde estão as oportunidades?*

### 🎯 Objetivos

- Praticar o fluxo completo de um projeto de análise de dados com **Python + Pandas**
- Aplicar boas práticas de **limpeza, tratamento e conversão de dados**
- Extrair **insights de negócio reais** a partir de dados de vendas
- Construir **visualizações claras e objetivas** para apoiar tomada de decisão
- Organizar o projeto seguindo **padrões profissionais** de estrutura e documentação

### 💼 Problema de Negócio

Times de e-commerce lidam diariamente com grandes volumes de dados de vendas, mas nem sempre conseguem transformar esses dados em decisões. Este projeto simula esse cenário: a partir de uma base de vendas, o objetivo é responder **onde investir esforço comercial, quais produtos priorizar e como está a evolução do faturamento ao longo do tempo**.

### 💡 Motivação

Projeto desenvolvido como prática de estudo em **Análise de Dados**, com foco em consolidar o ciclo completo de trabalho de um analista: geração/coleta → limpeza → exploração → visualização → insight. Ideal como peça de portfólio para demonstrar raciocínio analítico aplicado a um contexto de negócio real.

<br/>

---

## 🖼️ Demonstração

<div align="center">

### 💰 Faturamento por Estado
<img src="images/faturamento_estado.png" alt="Faturamento por Estado" width="700"/>

### 📅 Evolução Mensal do Faturamento
<img src="images/faturamento_mensal.png" alt="Faturamento Mensal" width="700"/>

### 🏆 Faturamento por Produto
<img src="images/faturamento_produto.png" alt="Faturamento por Produto" width="700"/>

### 📦 Quantidade Vendida por Produto
<img src="images/quantidade_produto.png" alt="Quantidade por Produto" width="700"/>

</div>

> 💬 *Todas as imagens acima são geradas automaticamente pelo notebook e salvas na pasta `images/`.*

<br/>

---

## ⚙️ Funcionalidades

- 🧪 **Geração de dataset sintético** de vendas de e-commerce via script Python
- 🧹 **Limpeza e tratamento de dados** (valores nulos, duplicados e inconsistências)
- 📆 **Conversão e padronização de datas** para análises temporais
- 🔎 **Análise exploratória de dados (EDA)** completa
- 💵 **Cálculo de faturamento por produto**
- 🗺️ **Cálculo de faturamento por estado**
- 📈 **Análise da evolução temporal das vendas**
- 📊 **Quantidade de produtos vendidos por categoria/item**
- 🖼️ **Geração e salvamento automático de gráficos** na pasta `images/`
- 📓 **Notebook documentado** com todo o passo a passo da análise

<br/>

---

## 🛠️ Tecnologias

<div align="center">

| Tecnologia | Finalidade |
|---|---|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | Linguagem principal do projeto |
| ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | Manipulação, limpeza e análise dos dados |
| ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat-square&logo=plotly&logoColor=white) | Criação das visualizações gráficas |
| ![Jupyter](https://img.shields.io/badge/-Jupyter%20Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white) | Ambiente interativo de análise |
| ![Git](https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white) | Controle de versão |
| ![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white) | Hospedagem e versionamento do código |

</div>

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
│   ├── faturamento_estado.png        # Gráfico de faturamento por estado
│   ├── faturamento_mensal.png        # Gráfico de evolução mensal do faturamento
│   ├── faturamento_produto.png       # Gráfico de faturamento por produto
│   └── quantidade_produto.png        # Gráfico de quantidade vendida por produto
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

<br/>

---

## 🚀 Como Executar

### ✅ Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/) instalado
- [Git](https://git-scm.com/) instalado

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/ederfelixsilva/analise-vendas-ecommerce.git
cd analise-vendas-ecommerce
```

### 2️⃣ Crie e ative um ambiente virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux/Mac
source venv/bin/activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Gere o dataset (opcional, caso queira recriar os dados)

```bash
python scripts/gerar_dados.py
```

### 5️⃣ Execute o notebook de análise

```bash
jupyter notebook notebooks/analise_vendas.ipynb
```

> 💡 Ao rodar todas as células do notebook, os gráficos serão gerados e salvos automaticamente na pasta `images/`.

<br/>

---

## 📈 Análises Realizadas

### 💰 Faturamento por Produto
Consolidação da receita total gerada por cada produto do catálogo, permitindo identificar quais itens são os principais motores de faturamento do negócio.

### 🗺️ Faturamento por Estado
Distribuição geográfica das vendas, evidenciando quais estados concentram maior volume de receita — informação estratégica para ações de marketing regional e logística.

### 📅 Evolução Temporal
Análise da série histórica de faturamento mês a mês, permitindo identificar tendências de crescimento, sazonalidade e possíveis quedas que merecem investigação.

### 📦 Quantidade Vendida por Produto
Análise do volume de unidades vendidas por produto, complementando a visão de faturamento com a perspectiva de demanda — útil para gestão de estoque e planejamento de compras.

<br/>

---

## 💡 Principais Insights

> Resumo executivo dos principais achados da análise:

- 🏆 **Concentração de receita**: uma parcela pequena do catálogo de produtos é responsável pela maior parte do faturamento total, sugerindo priorização de estoque e marketing nesses itens (padrão típico de curva de Pareto).
- 🗺️ **Disparidade regional**: o faturamento não está distribuído de forma homogênea entre os estados, indicando oportunidades de expansão em regiões com baixa penetração e potencial de mercado.
- 📈 **Tendência temporal**: a evolução mensal do faturamento revela períodos de crescimento e possíveis picos sazonais, informações relevantes para planejamento de campanhas e estoque futuro.
- 📦 **Volume x Receita**: produtos com alto volume de vendas nem sempre são os que mais faturam, reforçando a importância de olhar preço médio e ticket junto ao volume — não apenas a quantidade isolada.
- 🎯 **Oportunidade estratégica**: cruzar os dados de faturamento por estado com a evolução temporal pode direcionar decisões de investimento comercial mais assertivas por região e período.

<br/>

---

## 🔮 Melhorias Futuras

- [ ] 📊 Construção de **dashboard interativo no Power BI**
- [ ] 📉 Criação de **dashboard interativo com Plotly/Dash**
- [ ] 🗄️ Migração da análise para **SQL**, simulando um Data Warehouse
- [ ] 🤖 Aplicação de **Machine Learning** para previsão de vendas (forecasting)
- [ ] ☁️ **Deploy** da aplicação/dashboard em nuvem (Streamlit Cloud, Render ou similar)
- [ ] 🧪 Automatização de testes com **pytest** para as funções de tratamento de dados
- [ ] 🔄 Pipeline automatizado de **ETL** para atualização contínua dos dados

<br/>

---

## 🎓 Aprendizados

Este projeto foi fundamental para consolidar, na prática, o ciclo completo de um projeto de análise de dados:

- Aprofundamento no uso do **Pandas** para limpeza, transformação e agregação de dados
- Prática de **tratamento de datas** e séries temporais em Python
- Desenvolvimento de senso crítico para transformar números em **insights de negócio**
- Estruturação de um projeto de dados seguindo **boas práticas de organização e documentação**, pensando em legibilidade e manutenção
- Fortalecimento da comunicação técnica, ao transformar resultados analíticos em uma narrativa compreensível para públicos não técnicos

<br/>

---

## 👨‍💻 Autor

<div align="center">

### Éder Félix Silva

Estudante de Análise e Desenvolvimento de Sistemas | Front-end • Data Engineering • Cloud

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eder-f%C3%A9lix/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ederfelixsilva)

</div>

<br/>

---

<div align="center">

### ⭐ Se este projeto foi útil ou interessante para você, considere deixar uma estrela!

*Feito com 💙 e muitos `pd.groupby()` por Éder Félix Silva*

</div>
