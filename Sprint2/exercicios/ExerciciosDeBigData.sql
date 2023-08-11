-- Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. Utilizar o caractere ; (ponto e vírgula) 
-- como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos
-- nomes de cabeçalho que listamos abaixo:
-- CodLivro; Titulo; CodAutor; NomeAutor; Valor; CodEditora; NomeEditora.

select livro.cod as CodLivro, livro.titulo, livro.autor as CodAutor, autor.nome as NomeAutor, livro.valor, livro.editora as CodEditora, editora.nome as NomeEditora
from livro
left join autor on autor.codautor = livro.autor
left join editora on editora.codeditora = livro.editora
order by livro.valor desc
limit 10;
--------------------------------------------------------------------------------------------------------------
-- Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV.
-- Utilizar o caractere | (pipe) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e 
-- seus respectivos nomes de cabeçalho que listamos abaixo:
-- CodEditora; NomeEditora; QuantidadeLivros

with editora_livros as (
    select editora.codeditora, editora.nome, endereco.estado, endereco.cidade, count(livro.cod) as quantidade
    from editora
    left join livro on editora.codeditora = livro.editora
    left join endereco on editora.endereco = endereco.codendereco
    group by editora.codeditora, editora.nome, endereco.estado, endereco.cidade
    having count(livro.cod) > 0
)

select codeditora as CodEditora, nome as NomeEditora, quantidade as QuantidadeLivros
from editora_livros
order by quantidade desc
limit 5;