# Lab AWS Glue

## Bucket
O Bucket criado para o lab foi o **gllue**, como mostra a imagem:
![Bucket](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/buckets.png)

Dentro dele conforme o solicitado, no caminho **s3://gllue/lab-glue/input/nomes.csv** esta o arquivo csv, como mostra a imagem:
![Nomes.csv](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/nomes.png)

A gravação que dos resultados particionados esta de acordo no diretório **s3://gllue/lab-glue/frequencia_registro_nomes_eua/**, como mostra as imagens:
![Particionamento](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/particionado.png)
![Parte Feminina](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/F.png)
![Parte Masculina](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/M.png)


## AWS Glue
Na AWS Glue tem o database chamado **glue-lab**, conforme foi instruido e tambem o usuario que foi criado para poder fazer o processo.

![glue-lab](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/glue-lab.png)
![Usuario](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/usuario.png)


## Função/Role
Foi criado a função/role seguindo o nome que pede **AWSGlueServiceRole-Lab4** e tendo as 4 pemissões necessarioas, como mostra a imagem:
![Função/Rolse](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/funcao.png)


## Job
No job é onde ficou o script que rodou para fazer oque pedia, sendo esse o [Script](/Sprint7/Exercicios/Lab%20AWS%20Glue/script.scala). Seguindo o nome como pede:
![Job](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/job.png)


## Crawler
O Crawler criado seguindo tambem o nome corretamente de **FrequenciaRegistroNomesCrawler**
![Crawler](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/crawler.png)

Conforme fala la no pdf, esta dando pra consultar no Athena, como mostras a imagem:
![Athena](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/Athena.png)
![Saida](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/Saida.png)

Tambem foi dado as permissões para fazer SELECT e ver todos os dado:
![SELECT](/Sprint7/Exercicios/Lab%20AWS%20Glue/Imagens/select.png)