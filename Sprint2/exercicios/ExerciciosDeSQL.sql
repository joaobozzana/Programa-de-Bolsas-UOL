--------------------------------- EXERCICIOS DA BASE BIBLIOTECA ---------------------------------------------------


--------------------------------------- EXERCICIO 1 ---------------------------------------------------------------
-- Apresente a query para listar todos os livros publicados após 2014. 
-- Ordenar pela coluna cod, em ordem crescente, as linhas.  
-- Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma

select * 
from livro
where publicacao > '2015-0-0'
order by cod;

--------------------------------------- EXERCICIO 2 ---------------------------------------------------------------
--Apresente a query para listar os 10 livros mais caros. 
-- Ordenar as linhas pela coluna valor, em ordem decrescente.  
-- Atenção às colunas esperadas no resultado final:  titulo, valor.

select titulo, valor 
from livro
order by valor desc
limit 10;

--------------------------------------- EXERCICIO 3 ---------------------------------------------------------------
-- Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
-- O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
-- Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

with editora_livros as (
    select editora.codeditora, editora.nome, endereco.estado, endereco.cidade, count(livro.cod) as quantidade
    from editora
    left join livro on editora.codeditora = livro.editora
    left join endereco on editora.endereco = endereco.codendereco
    group by editora.codeditora, editora.nome, endereco.estado, endereco.cidade
    having count(livro.cod) > 0
)

select quantidade, nome, estado, cidade
from editora_livros
order by quantidade desc
limit 5;

--------------------------------------- EXERCICIO 4 ---------------------------------------------------------------
-- Apresente a query para listar a quantidade de livros publicada por cada autor. 
-- Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

select autor.nome, autor.codautor, autor.nascimento, count(livro.cod) as quantidade
from autor
left join livro on autor.codautor = livro.autor
group by autor.nome, autor.codautor, autor.nascimento
order by autor.nome;

--------------------------------------- EXERCICIO 5 ---------------------------------------------------------------
-- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil.
-- Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

SELECT DISTINCT autor.nome 
FROM autor
LEFT JOIN livro ON livro.autor = autor.codautor
LEFT JOIN editora ON editora.codeditora = livro.editora
LEFT JOIN endereco ON editora.endereco = endereco.codendereco
WHERE endereco.estado NOT IN ('RIO GRANDE DO SUL', 'PARANÁ')
ORDER BY autor.nome;

--------------------------------------- EXERCICIO 6 ---------------------------------------------------------------
-- Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

select autor.codautor, autor.nome, count(livro.cod) as quantidade_publicacoes
from autor, livro
where autor.codautor = livro.autor
group by autor.codautor, autor.nome
order by quantidade_publicacoes desc
limit 1;

--------------------------------------- EXERCICIO 7 ---------------------------------------------------------------
-- Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

select nome
from autor
left join livro on autor.codautor = livro.autor
group by autor.codautor, autor.nome
having count(livro.cod) = 0
order by autor.nome;




--------------------------------------- EXERCICIOS DA BASE LOJA-----------------------------------------------------


---------------------------------------------- EXERCICIO 8 ---------------------------------------------------------
-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  
-- As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

select tbvendedor.cdvdd, tbvendedor.nmvdd
from tbvendedor
join tbvendas on tbvendedor.cdvdd = tbvendas.cdvdd
group by tbvendedor.cdvdd, tbvendedor.nmvdd
order by count(tbvendas.cdven) desc
limit 1;

---------------------------------------------- EXERCICIO 9 ---------------------------------------------------------
-- Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. 
-- As colunas presentes no resultado devem ser cdpro e nmpro.

select tbvendas.cdpro, tbvendas.nmpro
from tbvendas
where tbvendas.dtven > '2014-02-03'
    and tbvendas.dtven < '2018-02-02'
    and tbvendas.status = 'Concluído'
group by tbvendas.cdpro, tbvendas.nmpro
order by count(tbvendas.cdven) desc
limit 1;

---------------------------------------------- EXERCICIO 10 --------------------------------------------------------
-- A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
-- O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. 
--O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

select tbvendedor.nmvdd as vendedor,
        SUM(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas,
        ROUND(SUM(tbvendas.qtd * tbvendas.vrunt) * tbvendedor.perccomissao / 100, 2) as comissao
from tbvendas
left join tbvendedor on tbvendedor.cdvdd = tbvendas.cdvdd
where tbvendas.status = 'Concluído'
group by tbvendedor.nmvdd
order by comissao desc;

---------------------------------------------- EXERCICIO 11 --------------------------------------------------------
-- Apresente a query para listar o código e nome cliente com maior gasto na loja. 
-- As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

select tbvendas.cdcli, tbvendas.nmcli, SUM(tbvendas.qtd * tbvendas.vrunt) as gasto
from tbvendas
where tbvendas.status = 'Concluído'
group by tbvendas.nmcli
order by gasto desc
limit 1;

---------------------------------------------- EXERCICIO 12 --------------------------------------------------------
-- Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). 
-- As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.

select tbdependente.cddep, tbdependente.nmdep, 
        tbdependente.dtnasc, 
        SUM(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas
from tbdependente 
left join tbvendedor on tbvendedor.cdvdd = tbdependente.cdvdd
left join tbvendas on tbvendas.cdvdd = tbvendedor.cdvdd
where tbvendas.status = 'Concluído'
group by tbdependente.nmdep, tbdependente.nmdep, tbdependente.dtnasc
having valor_total_vendas > 0
order by valor_total_vendas 
limit 1;

---------------------------------------------- EXERCICIO 13 --------------------------------------------------------
-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  
-- As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

select tbvendas.cdpro, tbvendas.nmcanalvendas, tbvendas.nmpro, SUM(tbvendas.qtd) as quantidade_vendas
from tbvendas
where (tbvendas.nmcanalvendas = 'Matriz' or tbvendas.nmcanalvendas = 'Ecommerce') and tbvendas.status = 'Concluído'
group by tbvendas.cdpro, tbvendas.nmcanalvendas, tbvendas.nmpro
order by SUM(tbvendas.qtd)
limit 10;

---------------------------------------------- EXERCICIO 14 --------------------------------------------------------
-- Apresente a query para listar o gasto médio por estado da federação.
-- As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

select tbvendas.estado, ROUND(AVG(tbvendas.qtd * tbvendas.vrunt), 2) as gastomedio
from tbvendas
where tbvendas.status = 'Concluído'
group by tbvendas.estado
order by gastomedio desc;

---------------------------------------------- EXERCICIO 15 --------------------------------------------------------
-- Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

select tbvendas.cdven
from tbvendas
where tbvendas.deletado <> 0
order by tbvendas.cdven;

---------------------------------------------- EXERCICIO 16 --------------------------------------------------------
-- Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. 
-- As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. 
-- Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).
--Obs: Somente vendas concluídas.

select tbvendas.estado, tbvendas.nmpro , ROUND(AVG(tbvendas.qtd), 4) as quantidade_media
from tbvendas
where tbvendas.status = 'Concluído'
group by tbvendas.estado, tbvendas.nmpro
order by tbvendas.estado;
--------------------------------------------------------------------------------------------------------------------