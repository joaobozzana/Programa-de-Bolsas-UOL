import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# @params:
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos para entrada e saída
source_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

import pandas as pd
from pyspark.sql import functions as F

df = spark.createDataFrame(pd.read_json(f"{source_path}part_0.json"))

for i in range(1, 11):
    arquivo_path = f"{source_path}part_{i}.json"
    df_arquivo = spark.createDataFrame(pd.read_json(arquivo_path))
    df = df.union(df_arquivo)

# Particionado por data de coleta do TMDB
caminho = source_path.split("/")
ano = caminho[len(caminho)-4]
mes = caminho[len(caminho)-3]
dia = caminho[len(caminho)-2]

df.write.parquet(f"{target_path}{ano}/{mes}/{dia}/TMDB")

job.commit()
