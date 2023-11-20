import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'SENHA','SENHASECRET'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

import boto3
import time

athena_client = boto3.client('athena', region_name='us-east-1', aws_access_key_id=args['SENHA'],
                             aws_secret_access_key=args['SENHASECRET'])

database_name = 'banco-refined'

queries = [
    """
    CREATE OR REPLACE VIEW dados_tmdb AS
    SELECT
        f.id_filme, f.titulooriginal,
        CASE WHEN f.avaliacao > 6 THEN 'Acima de 6' ELSE 'Abaixo de 6' END AS classificacao_nota,
        CASE WHEN f.receita > f.orcamento THEN 'Com Lucro' ELSE 'Com Prejuízo' END AS resultado_financeiro
    FROM
        filmes f;
    """,
    """
    CREATE OR REPLACE VIEW resultado_financeiro AS
    SELECT
        id_filme,
        titulooriginal,
        receita - orcamento AS resultado,
        CAST(
            CASE
                WHEN orcamento > 0 THEN 
                    CASE WHEN receita >= orcamento THEN (receita * 100.0 / orcamento) ELSE -1 * (receita * 100.0 / orcamento) END
                ELSE 0
            END AS DECIMAL(10, 2)) AS percentual
    FROM
        filmes;
    """,
    """
    CREATE OR REPLACE VIEW filmes_por_decada AS
    SELECT
        id_filme,
        titulooriginal,
        SUBSTRING(lancamento, 1, 3) || '0' AS decada
    FROM
        filmes
    ORDER BY
        decada DESC;
    """,
    """
    CREATE OR REPLACE VIEW desempenho_financeiro_por_decada AS
    SELECT
        (CAST(SUBSTRING(lancamento, 1, 3) AS INT) * 10) AS decada,
        SUM(CASE WHEN receita > orcamento THEN (receita - orcamento) ELSE 0 END) AS lucro_total,
        SUM(CASE WHEN receita <= orcamento THEN (receita - orcamento) ELSE 0 END) AS prejuizo_total,
        SUM(CASE WHEN receita > orcamento THEN (receita - orcamento) ELSE 0 END) - SUM(CASE WHEN receita <= orcamento THEN (receita - orcamento) ELSE 0 END) AS lucro_real
    FROM
        filmes
    WHERE
        TRY_CAST(SUBSTRING(lancamento, 1, 4) AS INT) IS NOT NULL
    GROUP BY
        (CAST(SUBSTRING(lancamento, 1, 3) AS INT) * 10)
    ORDER BY
        decada;
    """,
    """
    CREATE OR REPLACE VIEW desempenho_financeiro_por_ano AS
    SELECT
        EXTRACT(YEAR FROM CAST(lancamento AS DATE)) AS ano,
        SUM(CASE WHEN receita > orcamento THEN (receita - orcamento) ELSE 0 END) AS lucro_total,
        SUM(CASE WHEN receita <= orcamento THEN (receita - orcamento) ELSE 0 END) AS prejuizo_total,
        SUM(CASE WHEN receita > orcamento THEN (receita - orcamento) ELSE 0 END) - SUM(CASE WHEN receita <= orcamento THEN (receita - orcamento) ELSE 0 END) AS desempenho
    FROM
        filmes
    WHERE
        TRY_CAST(SUBSTRING(lancamento, 1, 4) AS INT) IS NOT NULL
        AND EXTRACT(YEAR FROM CAST(lancamento AS DATE)) >= 1980
    GROUP BY
        EXTRACT(YEAR FROM CAST(lancamento AS DATE))
    ORDER BY
        ano;
    """,
    """
    CREATE OR REPLACE VIEW avaliacoes_por_decada AS
    SELECT
        (CAST(SUBSTRING(lancamento, 1, 3) AS INT) * 10) AS decada,
        MIN(avaliacao) AS menor_avaliacao,
        AVG(avaliacao) AS media_avaliacao,
        MAX(avaliacao) AS maior_avaliacao
    FROM
        filmes
    WHERE
        TRY_CAST(SUBSTRING(lancamento, 1, 3) AS INT) IS NOT NULL AND SUBSTRING(lancamento, 1, 3) != ''
        AND avaliacao != 0  -- Adicionando a condição para não incluir avaliações iguais a 0
    GROUP BY
        (CAST(SUBSTRING(lancamento, 1, 3) AS INT) * 10)
    ORDER BY
        decada;
    """,
]

for query in queries:
    response = athena_client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': database_name},
        ResultConfiguration={'OutputLocation': 's3://desafio3/VIEW'}
    )

    query_execution_id = response['QueryExecutionId']

    max_attempts = 30
    while max_attempts > 0:
        response = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
        status = response['QueryExecution']['Status']['State']

        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break

        time.sleep(2)
        max_attempts -= 1

    if status == 'SUCCEEDED':
        print(f"A criação da view foi bem-sucedida.")
    else:
        print(f"A criação da view falhou com status: {status}")

        
    
job.commit()