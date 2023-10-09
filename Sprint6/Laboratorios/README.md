# Evidencias - Laboratórios

## Lab AWS S3

Bucket criado foi o **exemplodebucket.com** com acesso publico como mostra na imagem:
![Bucket](/Sprint6/Laboratorios/Lab%20AWS%20S3/Buckets.png)

Nele foram colocados os aquivos que foi pedido:
- 404.html -> Que seria um arquivo básico de erro
- indext.html -> Que seria o site
- dados/ -> Que seria a pasta onde fica o arquivo nomes.csv
- queries/ -> Que é a pasta para concluir o lab de Athena
- minha-camada-pandas.zip -> Que é um zip para concluir o Lab de Lambda

![Arquivos](/Sprint6/Laboratorios/Lab%20AWS%20S3/ArquivosBuckets.png)

E por fim o site funcionando

![Site](/Sprint6/Laboratorios/Lab%20AWS%20S3/Site.png)

---
## Lab AWS Athena

No lab de Athena é necessario criar um banco chamado meubanco e criar um tabela com atributos: nome, sexo, total e ano. O que mostra a imagem:

![Banco de Dados](/Sprint6/Laboratorios/Lab%20AWS%20Athena/Banco.png)

Foi proposto a seguinte consulta
- Crie uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje.

Onde foi utilizado o seguinte script

![Código](/Sprint6/Laboratorios/Lab%20AWS%20Athena/Codigo.png)

Arquivo SQL: [Código em SQL](/Sprint6/Laboratorios/Lab%20AWS%20Athena/codigo.sql);

Gerando o seguinte resultado:

![Código](/Sprint6/Laboratorios/Lab%20AWS%20Athena/ResultadoQuery.png)

---
## Lab AWS Lambda

Ja no lab de Lambda, por parte do Docker, segue as imagens da **imagem** e do **Dockerfile**

![Imagem](/Sprint6/Laboratorios/Lab%20AWS%20Lambda/Imagem.png)

![DockerFile](/Sprint6/Laboratorios/Lab%20AWS%20Lambda/DockerFile.png)

Da camada do Lambda

![Camada](/Sprint6/Laboratorios/Lab%20AWS%20Lambda/Camada.png)


E o resultado final, mostrando que esta tudo certo

![Resultado](/Sprint6/Laboratorios/Lab%20AWS%20Lambda/ResultadoLambda.png)
