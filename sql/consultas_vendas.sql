-- =========================================
-- ANÁLISE DE VENDAS DE E-COMMERCE
-- Consultas de negócio
-- =========================================


-- =========================================
-- 1. Produtos com maior faturamento
-- Pergunta:
-- Quais produtos geram mais receita?
-- =========================================

SELECT
    produto,
    SUM(faturamento) AS receita_total
FROM vendas
GROUP BY produto
ORDER BY receita_total DESC;


-- =========================================
-- 2. Faturamento por estado
-- Pergunta:
-- Quais estados possuem maior receita?
-- =========================================

SELECT
    estado,
    SUM(faturamento) AS receita_estado
FROM vendas
GROUP BY estado
ORDER BY receita_estado DESC;


-- =========================================
-- 3. Produtos mais vendidos
-- Pergunta:
-- Quais produtos possuem maior demanda?
-- =========================================

SELECT
    produto,
    SUM(quantidade) AS unidades_vendidas
FROM vendas
GROUP BY produto
ORDER BY unidades_vendidas DESC;


-- =========================================
-- 4. Evolução mensal do faturamento
-- Pergunta:
-- Como a receita evolui ao longo do tempo?
-- =========================================

SELECT
    strftime('%Y-%m', data) AS mes,
    SUM(faturamento) AS receita_mensal
FROM vendas
GROUP BY mes
ORDER BY mes;