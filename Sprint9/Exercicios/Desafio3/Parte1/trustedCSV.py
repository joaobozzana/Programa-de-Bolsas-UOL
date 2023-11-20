import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params:
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos para entrada e saída
source_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Leitura do CSV usando Spark
source_df = spark.read.option("header", "true").option("delimiter", "|").csv(source_path)

# Escrita em Parquet no S3
source_df.write.parquet(target_path)

job.commit()