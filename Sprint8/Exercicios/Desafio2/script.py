import pandas as pd
import requests
import os
import boto3
from datetime import date
import concurrent.futures
import io 
import json

def lambda_handler(event, context):
 
    # API
    api_key = os.environ.get('chaveTMDB')
    
    # CSV
    s3_client = boto3.client('s3')
    bucket = 'desafiio'
    s3_caminho = 'RAW/Local/CSV/Movies/2023/10/23/movies.csv'
    
    objeto = s3_client.get_object(Bucket=bucket, Key=s3_caminho)
    
    df = pd.read_csv(objeto['Body'], sep="|")
    
    # Filtrar por Terror e Mistério
    data = df[df['genero'].str.contains("Horror") & df['genero'].str.contains("Mystery")][['id', 'genero', 'anoLancamento']].drop_duplicates()
    
    #Lida com a API do TMBD
    def get_movie_info(movie_id):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        resposta = requests.get(url)
        data = resposta.json()
        return data
    
    filme = []
    
    # O trecho de código utiliza um ThreadPoolExecutor com 10 threads para buscar informações de filmes em paralelo, acelerando o processo de coleta de dados da API.
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        movie_ids = data['id'].tolist()
        results = list(executor.map(get_movie_info, movie_ids))
    
    for data in results:
        orcamento = data.get('budget')
        receita = data.get('revenue')
    
        if orcamento is not None and orcamento != 0 and receita is not None and receita != 0: # Filtro pra pegar somente oque tem orçamento e receita
            filme.append({'id': data['id'],
                          'lancamento': data['release_date'],
                          'orcamento': orcamento,
                          'receita': receita,
                          'avaliacao': data['vote_average']})
    
    # Variareis subir pro bucket
    camada = 'RAW'
    origem = 'TMDB'
    formato = 'JSON'
    today = date.today()
    data_de_processamento = today.strftime("%Y/%m/%d")
    
    cont = 0
    df_particionado = []
    
    # fors de particionamento, com no maximo 100
    for i in range(0, len(filme), 100):
        if i + 100 < len(filme):
            df_part = pd.DataFrame(filme[cont:i + 100])
        else:
            df_part = pd.DataFrame(filme[cont:len(filme)])
        cont = i + 100
    
        df_particionado.append(df_part)
    
    for i in range(len(df_particionado)):
        # Crie um nome de caminho exclusivo para cada pedaço
        target_path = f"{camada}/{origem}/{formato}/{data_de_processamento}/part_{i}.json"
        
        arquivo = io.StringIO()
        X = df_particionado[i].to_json(arquivo)
        
        # Faça o upload do DataFrame particionado para o Amazon S3
        s3_client.put_object(Body = arquivo.getvalue(), Bucket = bucket, Key = target_path)

    return {
        'status code': 200,
        'body': json.dumps(f"Funcionou")
    }
