# Comandos usados

## Docker

Buildar o docker

- `docker build -t camadapandas .` -> Criando a imagem
- `docker run -it camadapandas` -> Criando o container

Criando pasta pra zipar
- `bash-4.2# cd root`
- `bash-4.2# mkdir camadadesafio`
- `bash-4.2# cd camadadesafio`
- `bash-4.2# mkdir python`
- `bash-4.2# cd python`
- `bash-4.2# pwd`
- /root/camadadesafio/python

Instalando oque precisa na pasta
- `pip install pandas -t .`
- `pip install requests -t .`
- `pip install urllib3==1.26.6 -t .`
- `zip -r python.zip python`

Copiando pra local e subir no s3
- `docker ps`
- `docker cp c88d:/root/camadadesafio/python.zip ./ `