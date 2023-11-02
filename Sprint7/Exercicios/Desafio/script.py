import boto3
from datetime import date

client = boto3.client(
    's3', 
    aws_access_key_id = "AKIA4Q3QQNO5BW45FYGI", #Chave invalidada 
    aws_secret_access_key = "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", #Chave invalidada 
)

today = date.today()
bucket_name = 'desafiio'
camada = 'RAW'
origem = 'Local'
data_de_processamento = today.strftime("%Y/%m/%d")


movies = open('movies.csv', 'rb')
series = open('series.csv', 'rb')

formato_dado = 'CSV'

tipoM = 'Movies'
target_pathM = f"{camada}/{origem}/{formato_dado}/{tipoM}/{data_de_processamento}/movies.csv"

tipoS = 'Series'
target_pathS = f"{camada}/{origem}/{formato_dado}/{tipoS}/{data_de_processamento}/series.csv"

client.upload_fileobj(movies, bucket_name, target_pathM)
client.upload_fileobj(series, bucket_name, target_pathS)