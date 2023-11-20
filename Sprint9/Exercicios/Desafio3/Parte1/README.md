# Tarefa 3: Desafio Parte 3 - Processamento da Trusted

Com essa proposta, foram criados dois scripts: um para o arquivo em CSV e outro para os arquivos em JSON que foram gerados na Sprint anterior.

No caso dos arquivos JSON, uma consideração importante foi respeitada:
- Todos os dados serão persistidos na Trusted no formato PARQUET, particionados por data de coleta do TMDB (dt=< ano-mês-dia >, por exemplo, dt=2023-11-31).

---
### CSV

O arquivo script pro CSV é esse: [trustedCSV.py](trustedCSV.py).

### JSON

O arquivo de script para os JSON é este: [trustedJSON.py](trustedJSON.py). Nele, há um detalhe importante em que foi necessário utilizar o pandas, porém, criando o DataFrame no Spark. Isso se deve ao fato de que no código da Sprint anterior, os JSON foram carregados utilizando o pandas, o que causava dificuldades para o Spark ler corretamente os dados. Embora houvesse a possibilidade de corrigir isso e rodar novamente, optou-se por deixar como aprendizado, lidando com desafios que podem surgir durante o processo.

---
### Athena 

Por fim, criei um **Crawler** para visualizar no Athena se os dados estão corretos e se foram particionados em formato .parquet conforme o esperado.

O banco foi criado corretamente, com a tabela **csv** contendo os dados do arquivo **CSV** e a tabela **tmdb** contendo os dados salvos em formato **JSON**, como demonstrado na imagem: 

![Banco](/Sprint9/Exercicios/Desafio3/Parte1/imgs/banco.png)

---

Na tabela **csv** os dados do CSV estão todos presentes, como mostra as imagens:

Comando: `select count(*) from csv`
![Count CSV](/Sprint9/Exercicios/Desafio3/Parte1/imgs/countCSV.png)

Comando: `select * from csv`
![Tabela CSV](/Sprint9/Exercicios/Desafio3/Parte1/imgs/tabelaCSV.png)

---

Na tabela **tmdb** ficou os dados JSON, a quantidade bate certinho com oque foi gerado, como mostra as imagens:

Comando: `select count(*) from tmdb`
![Count CSV](/Sprint9/Exercicios/Desafio3/Parte1/imgs/countJSON.png)

Comando: `select * from tmdb`
![Tabela CSV](/Sprint9/Exercicios/Desafio3/Parte1/imgs/tabelaJSON.png)