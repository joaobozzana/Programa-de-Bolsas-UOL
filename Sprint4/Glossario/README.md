## Glossário com mais comandos úteis de docker

### Container

**docker ps** -> mostra os container rodando;

**docker ps -a** -> mostra todos os containers que já rodaram;

**docker run < nome >** -> inicia o container;

**docker run -it < nome >** -> inicia o container e deixa ele ativo;

**docker run -d < nome >** -> executa o container em background;

**docker stop < id_ou_nome >** -> para um container que esta rodando;

**Docker start < id >** -> retoma o container;

**docker run -d -p 80:80** -> deixa o container acessível na porta 80 (para entrar no localhost);

EX: 3000:80 / 80 do container na porta 3000 do pc, logo seria localhost:3000

**docker run -d -p 80:80 --name nginx_app nginx** -> dou um nome para o container;

**docker logs < nome_do_container >** -> mostra os logs do container;

**docker rm < id_ou_nome >** -> remove o container;

**docker rm < id_ou_nome > -f** -> força a remoção;

**docker run -d –rm < nome_do_container >** -> quando parar é removido;

**docker start -i meucontainr** -> serve pra iniciar o container de modo interativo;

**docker cp < container >:< caminho_do_arquivo > < caminho_que_quero_copiar >** -> copiar um arquivo de um container;

**docker top < container >** -> mostra alguns status do container;

**docker inspect < container >** -> mostra informações como id, data de criação, imagem, etc;

**docker stats** -> mostra informações como consumo de cpu, MEM, transferência de rede;

---
### Imagens

**docker tag < id > minhaimagem** -> troca o nome da imagem;

**docker tag < id > minhaimagem:minhatag** -> cria uma tag pra imagem;

OBS: tag faz uma outra versão da imagem

**docker -t nomequeeuquero .** -> cria uma imagem com o nome desejado;

**docker rmi < id >** -> remove a imagem;

**docker rmi -f < id >** -> força a remover a imagem;

**docker build .** -> é usado para construir uma nova imagem Docker a partir de um Dockerfile;

---
### Geral

**docker system prune** -> remove container e imagens que não esta sendo utilizados;

**Docker run –help** -> ver todos os comandos;

---
### Docker HUB
**docker login** -> entra no docker hub;

**docker logout** -> sai do docker hub;

**docker push imagem** -> envia a imagem para o hub (tem que estar autenticado);

**docker pull imagem** -> puxa a imagem, faz download;

---
### Compose
**docker-compose up** -> iniciar o Docker composse;

OBS: docker-compose é o nome do arquivo.yaml

**docker-compose up -d** -> tira os logs e roda em background;

**docker-compose down** -> para o compose que esta rodando em background;
