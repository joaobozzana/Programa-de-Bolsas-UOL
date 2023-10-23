# Tarefa 2: Apache Spark - Contador de Palavras

Pra criar a imagem usei o comando:
* docker pull jupyter/all-spark-notebook
----
Pra rodar a imagem no container, utilizei o comando:
* docker run -p 8888:8888 jupyter/all-spark-notebook
---
Pra puxar o README.md, eu criei um repositório publico com ele, ai utilizei o seguinte comando:
* docker exec bcfa wget "https://raw.githubusercontent.com/joaobozzana/tarefa2/main/README.md"
---
Pra inciar o spark-shell, foi o comando:
* docker exec -it bcfa spark-shell
---
O código para fazer o contador de palavras esta aqui [Código](/Sprint7/Exercicios/Tarefa2/Spark.scala)

Que deu o seguinte resultado

![Resultado](/Sprint7/Exercicios/Tarefa2/resutlado.png)