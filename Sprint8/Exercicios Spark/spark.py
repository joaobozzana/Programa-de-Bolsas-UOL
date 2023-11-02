from pyspark.sql import SparkSession
from pyspark.sql.functions import when, rand, expr
from pyspark import SparkContext, SQLContext
import random

#------------------------------------ Passo 1 e 2 ---------------------------------------#
spark = SparkSession \
        .builder \
        .master("local[*]")\
        .appName("spark.py") \
        .getOrCreate()

df = spark.read.text("nomes_aleatorios.txt")

# Renomeie a coluna para "Nomes"
df = df.withColumnRenamed("value", "Nomes")

# Exiba o schema atualizado
df.printSchema()

#------------------------------------ Passo 3 ------------------------------------------#
# Por escolaridade de forma aleatória
df = df.withColumn("Escolaridade", when(rand() < 0.33, "Fundamental")
                                           .when((rand() >= 0.33) & (rand() < 0.66), "Médio")
                                           .otherwise("Superior"))

#------------------------------------ Passo 4 ------------------------------------------#
# Por os 13 paises da América do Sul
paises = ["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"]

def pais_aleatorio():
    return random.choice(paises)

spark.udf.register("pais_aleatorio", pais_aleatorio)
df = df.withColumn("Pais", expr("pais_aleatorio()"))

#------------------------------------ Passo 5 ------------------------------------------#
# Por a coluna ano
df = df.withColumn("AnoNascimento", expr("CAST(1945 + rand() * (2011 - 1945) AS INT)"))

#------------------------------------ Passo 6 ------------------------------------------#
# Filtra pelo século
df_select = df.filter(df.AnoNascimento >= 2000)

# Mostre 10 nomes das pessoas que nasceram neste século
df_select.select("Nomes").show(10)

#------------------------------------ Passo 7 ------------------------------------------#
# Registre o DataFrame como uma tabela temporária
df.createOrReplaceTempView("pessoas")

# Execute o comando SQL para selecionar as pessoas que nasceram neste século
query = "SELECT Nomes FROM pessoas WHERE AnoNascimento >= 2000"
df_select = spark.sql(query)

# Mostre 10 nomes das pessoas selecionadas
df_select.show(10)

#------------------------------------ Passo 8 ------------------------------------------#
# Geração Millennials
df_millennials = df.filter((df.AnoNascimento >= 1980) & (df.AnoNascimento <= 1994))

# Conte o número de pessoas na geração Millennials
count_millennials = df_millennials.count()

print("Número de pessoas da geração Millennials:", count_millennials)

#------------------------------------ Passo 9 ------------------------------------------#
df.createOrReplaceTempView("pessoas")

query = "SELECT COUNT(*) AS TotalMillennials FROM pessoas WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994"
result = spark.sql(query)

result.show()

#------------------------------------ Passo 10 -----------------------------------------#
# Registre o DataFrame como uma tabela temporária
df.createOrReplaceTempView("pessoas")

#  Baby Boomers – nascidos entre 1944 e 1964
query_boomers = """
                SELECT Pais, 'Baby Boomers' AS Geracao, COUNT(*) AS Quantidade
                FROM pessoas
                WHERE AnoNascimento >= 1944 AND AnoNascimento <= 1964
                GROUP BY Pais
                """

#  Geração X – nascidos entre 1965 e 1979
query_gen_x = """
                SELECT Pais, 'Geração X' AS Geracao, COUNT(*) AS Quantidade
                FROM pessoas
                WHERE AnoNascimento >= 1965 AND AnoNascimento <= 1979
                GROUP BY Pais
                """

# Millennials (Geração Y) – nascidos entre 1980 e 1994;
query_millennials = """
                    SELECT Pais, 'Millennials' AS Geracao, COUNT(*) AS Quantidade
                    FROM pessoas
                    WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994
                    GROUP BY Pais
                    """

# Geração Z – nascidos entre 1995 e 2015.
query_gen_z = """
                SELECT Pais, 'Geração Z' AS Geracao, COUNT(*) AS Quantidade
                FROM pessoas
                WHERE AnoNascimento >= 1995 AND AnoNascimento <= 2015
                GROUP BY Pais
                """

# Combine os resultados em um novo DataFrame
df_result = spark.sql(query_boomers).union(spark.sql(query_gen_x)).union(spark.sql(query_millennials)).union(spark.sql(query_gen_z))

# Ordene o novo DataFrame em ordem crescente de Pais, Geração e Quantidade
df_result = df_result.orderBy("Pais", "Geracao", "Quantidade")

# Mostre todas as linhas do DataFrame resultante
df_result.show()
