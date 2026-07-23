-- =========================================
-- ANÁLISES DE NEGÓCIO
-- E-commerce Analytics
-- =========================================


-- =========================================
-- 1. Receita total do negócio
-- Pergunta:
-- Qual foi o faturamento total?
-- =========================================

SELECT
    SUM(faturamento) AS faturamento_total
FROM vendas;



-- =========================================
-- 2. Ticket médio por venda
-- Pergunta:
-- Qual o valor médio das vendas?
-- =========================================

SELECT
    AVG(faturamento) AS ticket_medio
FROM vendas;



-- =========================================
-- 3. Quantidade total vendida
-- Pergunta:
-- Quantas unidades foram vendidas?
-- =========================================

SELECT
    SUM(quantidade) AS total_unidades
FROM vendas;



-- =========================================
-- 4. Ranking de estados
-- Pergunta:
-- Quais regiões possuem maior participação?
-- =========================================

SELECT
    estado,
    SUM(faturamento) AS receita,
    COUNT(*) AS quantidade_vendas
FROM vendas
GROUP BY estado
ORDER BY receita DESC;



-- =========================================
-- 5. Produtos com maior volume e receita
-- Pergunta:
-- Quais produtos possuem melhor desempenho?
-- =========================================

SELECT
    produto,
    SUM(quantidade) AS unidades,
    SUM(faturamento) AS receita
FROM vendas
GROUP BY produto
ORDER BY receita DESC;