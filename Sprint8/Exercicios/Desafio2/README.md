# Comandos usados

## Docker

Buildar o docker

- `docker build -t camadapandas .` -> Criando a imagem
- `docker run -it camadapandas bash` -> Criando o container

Criando pasta pra zipar
- `bash-4.2# cd root` -> Acessando pasta
- `bash-4.2# mkdir camadadesafio` -> Criando pasta
- `bash-4.2# cd camadadesafio` -> Acessando pasta
- `bash-4.2# mkdir python` -> Criando pasta
- `bash-4.2# cd python` -> Acessando pasta
- `bash-4.2# pwd` -> Ver caminho
- /root/camadadesafio/python -> Ultimo caminho

Instalando oque precisa na pasta
- `pip install pandas requests urllib3==1.26.6 -t .` -> Instalando tudo que precisa
- `zip -r python.zip .` -> Zipa a pasta

Copiando pra local e subir no s3
- `docker ps` -> Vero id do meu container
- `docker cp c88d:/root/camadadesafio/python.zip ./ ` -> Copiando pra maquina local

## Script.py

No Script esta [aqui](/Sprint8/Desafio2/script.py) onde de mais relevante foi a filtragem nas categorias Terror e Mistério, alem disso eu cortei os filmes ja que não tenha orçamento nem receita, pois é essencial pra minha pesquisa