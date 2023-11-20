import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_CSV', 'S3_INPUT_PATH_TMDB', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos para entrada e saída
source_path_csv = args['S3_INPUT_PATH_CSV']
source_path_tmdb = args['S3_INPUT_PATH_TMDB']
target_path = args['S3_TARGET_PATH']

from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

# Leitura dos DataFrames
df_csv = spark.read.format("parquet").load(source_path_csv)
df_tmdb = spark.read.format("parquet").load(source_path_tmdb)

# Tabelas que vem dos parques 
df_csv.createOrReplaceTempView("tabela_csv")
df_tmdb.createOrReplaceTempView("tabela_tmdb")

# df_csv.show()
# df_tmdb.show()

# Criando as novas tabelas ja normalizadas
Filme = """
    SELECT DISTINCT
        csv.id AS id_filme,
        csv.titulooriginal,
        csv.tempominutos,
        csv.genero,
        csv.numerovotos,
        tmdb.lancamento,
        tmdb.avaliacao,
        tmdb.orcamento,
        tmdb.receita
    FROM tabela_tmdb AS tmdb
    LEFT JOIN tabela_csv AS csv ON csv.id = tmdb.id
    """
tab_filme = spark.sql(Filme)
tab_filme.createOrReplaceTempView("tab_filme")

#tab_filme.show()
#print(tab_filme.count())

Ator = """
    SELECT DISTINCT 
        nomeartista AS nome, anonascimento, anofalecimento, profissao, generoartista AS genero
    FROM tabela_csv, tab_filme
    WHERE tabela_csv.id = tab_filme.id_filme
    """
tab_ator = spark.sql(Ator)
tab_ator = tab_ator.withColumn("id_ator", monotonically_increasing_id())
tab_ator.createOrReplaceTempView("tab_ator")

#tab_ator.show()
#print(tab_ator.count())

FilmeAtor = """
    SELECT DISTINCT
        a.id_ator, f.id_filme, c.personagem
    FROM tab_filme f, tabela_csv c, tab_ator a
    WHERE f.id_filme = c.id AND a.nome = c.nomeartista 
    """
tab_filmeator = spark.sql(FilmeAtor)
tab_filmeator.createOrReplaceTempView("tab_filmeator")

#tab_filmeator.show()
#print(tab_filmeator.count())

tab_filme.write.parquet(f"{target_path}/filmes/")
tab_ator.write.parquet(f"{target_path}/atores/")
tab_filmeator.write.parquet(f"{target_path}/filmeator/")


job.commit()