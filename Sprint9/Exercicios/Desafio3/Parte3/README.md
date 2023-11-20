# Tarefa 5: Desafio Parte 3 - Processamento da Refined

Na minha tarefa, criei um banco de dados com três tabelas. Separei os atores em uma tabela e os filmes em outra, que é a parte do meu interesse. Como é uma relação muitos para muitos, foi necessário criar uma tabela intermediária entre os dois. Além disso, desenvolvi seis views até o momento, fornecendo informações úteis para minhas futuras análises:

- dados_tmdb: Apresenta dados práticos referentes ao TMDB de maneira geral.
- filmes_por_decada: Exibe os filmes agrupados por década.
- resultado_financeiro: Mostra se um filme teve lucro ou prejuízo, incluindo a porcentagem correspondente.
- avaliacoes_por_decada: Apresenta as avaliações mínimas, máximas e médias dos filmes por década.
- desempenho_financeiro_por_ano: Fornece detalhes do desempenho financeiro com valores mais específicos por ano.
- desempenho_financeiro_por_decada: Detalha o desempenho financeiro com valores específicos por década.

![Banco Refined](/Sprint9/Exercicios/Desafio3/Parte3/imgs/banco-refined.png)

O job criado para realizar esse processo de receber os dados dos parques, manipulá-los e salvá-los conforme desejado em tabelas é o seguinte: [tabelas](refined.py).

Ja o job criado para criar as views é o seguinte: [views](refinedviews.py).

Vale ressaltar que para a criação das views foi utilizado do boto3, ja que utilizando o spark por algum motivo mesmo gerando no datalog, ele não aparecia no Athena, as tabelas aparecem, mas as views não.