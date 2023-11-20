# Tarefa 4: Desafio Parte 3 - Modelagem de dados da Refined

## Tabelas, após a normalização

Na parte de tabelas, foi necessário criar apenas três tabelas: uma para os **atores**, outra para os **filmes**, e uma terceira chamada **filmeator** para estabelecer a relação muitos para muitos entre eles. Essa abordagem foi adotada para separar os dados do CSV, concentrando o foco principalmente nos filmes, mas mantendo a inclusão dos atores para eventual uso futuro.

Na tabela de **filmes**, alguns dados foram removidos, e foram incorporadas informações da tabela do TMDB. O código para essa operação é o seguinte: [tabelas.sql](tabelas.sql).

Aqui está a imagem do modelo gerado:

![Tabelas](/Sprint9/Exercicios/Desafio3/Parte2/imgs/tabelasDesafio.png)

## Fatos e dimensões

Foram criadas 6 tabelas, sendo 5 de dimensões e 1 de fato, que me ajudarão mais adiante. Todas estão neste arquivo: [views.sql](views.sql).

Aqui está a imagem do modelo gerado:

![Views](/Sprint9/Exercicios/Desafio3/Parte2/imgs/viewsDesafio.png)