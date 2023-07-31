# Glossário dos resumos, abordando os comandos e suas variações.



## Curso de Git e GitHub do básico ao avançado (c/ gist e GitHub Pages)

### Git: comandos basicos

**git status** -> ver o status de modificções não realizadas ainda

**git add <arquivo>** -> são adicionados ao projeto e deixa os arquivos prontos para ser commitados;

**git add .** -> vai todos;

**git comit -a -m “texto”** -> faz o commit dos códigos adicionas pelo comando anterior;

**git push** -> enviar o código pro repositório;

**git pull** -> recebe alterações do repositório;

**git clone https....** -> clonar repositório;

**git rm _arquivo_**-> deleta um arquivo;

**git log** -> ver histórico de commits e etx;

**git mv**  ->  move ou renomeia um arquivo;

**git chekout _arquivo_** -> desfaz as alterações feitas no arquivo;

### Git: controle de branch

**git branch** -> Listar as Branch do repositório;

**git branch <NOME_DA_BRANCH>** -> Criar um Branch nova no repositório;

**git branch -d <NOME_DA_BRANCH>** -> deletar a Branch desejada;

**git checkout <NOME_DA_BRANCH>** -> muda de Branch para branch;

**git checkout -b <NOME_DA_BRANCH>** -> criar uma Branch e já mudar pra ele;

**git merge <NOME_DA_BRANCH>** -> mesclar as Branch, exemplo seria pra puxar as 
atualizações da master;

**git fetch -a** -> buscar novas Branch que VS não esta vendo;

**OBS: se tiver alteração e mudar de Branch, as alterações vai junto. Sempre partir da master caso va criar uma nova.**

### Git: Stash (descartar aquivos, mas deixando passivel de recuperação)

**git stash** -> reseta as alterações voltando com a versão do repositório (mas salva as alterações em stash);

**git stash list** -> lista as stash ;

**git stash apply _id_da_Stash_** -> recebe os dados da stash;

**git stash show -p _id_da_Stash_** -> mostra as alterações que tem nela;

**git stash drop _id_da_Stash_** -> para limpar a stash;

**git stash clear** -> limpar todas as stash;


### Git: Tags (checkpoint de branchs)

**git tag -a _nome_ -m _mensagem_** -> criar uma tag; 

**git tag** -> listar as tag;

**git tag show _qual tag_** -> ver as alterações da tag;

**git checkout _nome da tag_** -> voltar pra tag que deseja;

**git push origin _nome-da-tag_** -> enviar a TAG para o repositório;

**git push origin –tags** -> envia todas as tags;

### Git: outros comandos

**git diff _arquivo1_ _arquivo2_** -> compara arquivos, ver a diferença;

**git shortlog** -> ver os últimos comits;

**git reflog** -> mapeia tudo no repositório;

**git archive –format zip –output <nome_desejado.zip> _main_** -> zipar o repositório;

**git rebase _<Branch-do-repositorio>_ _privat-branch_** -i -> Criar branch private;

**pick** -> seria levar todos os comits com sua mensagem;

**squash** -> excluir a mensagem e fazer merge com outros comit;

**reword** -> renomear o texto do comit;

### GitHub: entendendo suas pages

**Code** -> código do projeto;

**Issues** -> criar tarefas a serem desenvolvidas ou homologar bugs; 

**Projects** -> possível criar quadro de tarefas, meio que na mesma pegada que o trello por exemplo; oque permite um controle melhor na organização com o time;

**Wiki** -> documentação do projeto mais extensa;

**Insights** -> relatório geral do projeto, como pull request finalizados e abertos:  tags, issues, comits, contribuidores, entre outros;

**Gist** -> criação de códigos de soluções simples e objetivo (mini repositórios);


--------------------------------------------------------------------------------------
## Linux

### Linux: conhecendo diretórios da raiz

**bin** -> contem arquivos binários, como exemplo o próprio shell;

**boot** -> auxilia na inicialização do sistema;

**dev** -> arquivos que representa todos os dispositivos de entrada e saída;

**etc** -> arquivos de configurações;

**home** -> usuários do SO;

**lib** -> contem arquivos de bibliotecas;

**media** -> responsável para apresentar as pastas ;

**opt** -> arquivos de terceiros;

**sbin** -> arquivos binários de inicialização do sistema;

**tmp** -> arquivos temporários (descartáveis);

**usr** -> contem arquivos de apenas modo leitura (manual do sistema);

**var** -> arquivos de log;

### Linux: comandos básicos para a navegação pelo shell e suas variações

#### Comando cd:
**cd _diretório_** -> vai para o diretório;

**cd ..** -> sobe um diretório;

**cd ../../../** -> a cada ../ volta um diretório;

**cd /** -> cair na raiz dos arquivos;

**cd -** -> leva para o último diretório que estava;

**cd ~** -> vai pra pasta home do usuário;

#### Comando ls:
**ls** -> lista diretórios e arquivos;

**ls -l** -> detalha mais, onde mostra permissões de arquivos, usuário e grupo, tamanho e data de criação;

**ls -a** -> mostra arquivos ocultos;

**ls -ltr** -> (tr) mostra a data de modificação dos arquivos;

**ls -R** -> mostra os sub-diretórios de cada pasta;

#### Comando cat:
**cat _arquivo__** -> exibe o conteúdo do arquivo;

**cat _arquivo1_ _arquivo2_** -> exibe o conteúdo de 2 arquivos;

**cat _arquivo1_ _arquivo2_ > _arquivo3_** -> cria um arquivo 3 com o conteúdo do arquivo 1 e 2;

**cat _arquivo1_ >> _arquivo2_** -> concatena o conteúdo de arquivo1 com o de arquivo2;

#### Comando touch: criar arquivos
**touch _arquivo_** -> cria um arquivo;

**touch a.txt b.txt c.txt** -> concatenar criação de arquivos;

#### Comando mkdir: criar diretórios
**mkdir _nome do diretório_** - criar o diretório;

**mkdir _pasta1_ _pasta2_ _pasta3_ _pasta4_** -> concatena a criação de vários diretórios;

**mkdir -p dir1/dir2/dir3/dir4** -> cria diretórios dentro de diretórios;

### Linux: remover  (rm), copiar (cp) e movimentar (mv)
**rm _arquivo_** -> remove o arquivo;

**rm -dv _diretório_** -> remove o diretório vazio;

**rm -rfv _diretório_** -> remove diretórios com conteúdo, removendo tudo dentro do diretório;

**cp _arquivo_ _arquivo2_** -> cria arquivo 2 como cópia de arquivo;

**cp _arquivo_ _arquivo2_ _arquivo3_ _diretório_** -> copia os arquivos para o diretório;

**cp -r _diretorio1_ _diretorio2_** -> copia um diretório para o outro;

**cp -r _diretório-copiado/*_ _diretório-destino_** -> copia tudo de um diretório para o outro;

**mv _arquivo1_ _arquivo2_** -> renomeia o arquivo;

**mv _arquivo_ _diretório>/_** -> mover arquivos para diretórios;

### Linux: busca com grep e find + locate
**grep _texto-deseja_ _documento_** -> busca texto especifico (case sensitive);

**grep -i** -> tira o case sensitive;

**grep _texto-desejado_ -r** -> busca nas pastas e pastas dentro das pasta;

**find -name _doc.txt_** -> procurar o nome do arquivo;

**find -iname _doc.txt_** -> tira o case sensitive;

**locate _doc.txt_** -> mostra o caminho do doc desejado, mas n atualiza em tempo real;

### Linux: editores de texto nano e vim
**nano _arquivo_** -> abre o arquivo para as edições;

**alt a** -> seleciona o texto pra copiar // **alt 6** -> copia o texto selecionado // **Ctrl u** = cola o texto;

**alt a** -> seleciona o texto pra copiar // **Ctrl k** -> recorta o texto selecionado // **Ctrl u** = cola o texto;

#### atalhos do nano
**alt /** = ir pro fim do arquivo // **alt \ '** = ir pro começo do arquivo // **alt g linha** -> vai pra linha que deseja // **ctrl w** -> procurar oque deseja (palavra ou frases) // **ctrl o** = salvar o arquivo // **ctrl x** = sair do nano;


**vim _arquivonovo_** -> cria um arquivo;

#### atalhos do vim
**i** abre o modo de edição // **Esc** volta pro modo leitura // **:x** -> salva e sai do arquivo // **Ed** -> deleta a linha // **D (setinha pra cima)** -> deleta pra cima // **D (setinha pra baixo)** -> deleta pra baixo // **U** -> desfazer // **ctrl r** -> refazer // **/palavra** -> busca palavra // **n** -> avança // **shift n** -> ele volta // **%s/palavra/PALAVRANOVA/g** -> substituí tudo // **s/palavra/PALAVRANOVA/g** -> substituí da linha;

### Linux: gerenciamento de usuarios e grupo
**sudo adduser usuário** -> criar usuário;

**sudo userdel –remove usuário** -> deletar usuário;

**sudo usermod -l roberta -d /home/roberta -m maria** -> modificar nome dos usuários;

habilitar e desabilitar usuário: **sudo usermod -L usuario** (desabilita) //  **sudo usermod -U usuario** (habilita);

**getent group** -> lista todos os grupos;

**groups _usuario_** -> ver qual grupo o usuário esta;

**sudo groupadd -g _id_ _nome_** -> criar um grupo;

**sudo groupdel _nome_** -> deletar um grupo;

**sudo usermod -a -G _grupo_ _usuario_** ->  colocar usuário em um novo grupo;

**sudo gpasswd -d _usuario_ _grupo_** -> remover o usuário de um novo grupo;

**passwd** -> alterar a senha do usuário;

### Linux: permissões (forma numérica)
**Leitura: R** (Somente ler o arquivo) //
**Escrita: W** (escrever e alterar o arquivo) //
**Execução: X** (executar o arquivo como scripts) 

EX: 1 222 333 444

1. 1: diretório ou arquivo;

2. 222: permissões do owner (dono do arquivo);

3. 333: permissões do grupo (que o arquivo pertence);

4. 444: permissões dos demais usuários (que não são os donos e n fazem parte do grupo do arquivo);

O trio de caracteres é referente as permissões Leitura, Escrita e Execução;
* D: diretório ;
* ' - ' : arquivo;
* R: read = ler;
* W: write = escrever/editar;
* X: executar = executar;
* ' - ' : não há permissão;

Alteração em modo numérico
**chmod xxx arquivo/diretório** (1° x pro owner, 2° x para grupo, 3° x para os demais)
* 0: sem permissão : ---
* 1: Executar –x
* 2: Escrever -w-
* 3: Escrever e Executar -wx
* 4: Ler r—
* 5: Ler e Executar r-x
* 6: Ler e escrever rw-
* 7: Ler, escrever e executar rwx

**chown NovoUser arquivo.txt** -> Altera o dono do arquivo/diretório;

**chown NovoUser:NovoGrupo arquivo.txt** -> Altera o dono e o grupo do arquivo/diretório;

**chgrp grupo arquivo.txt** -> Alterar somente o grupo do arquivo

### Linux: compactar e descompactar
Compactar -> **tar -czvf compactar.tar.gz pasta**
(c: criar; z: comprimir em gz; v: ver processo; f: especificar o nome)

Compactar vários -> **tar -czvf compactar.tar.gz pasta1 pasta2 arquivo1 arquivo2**;

Descompactar -> **tar -xzvf compactar.tar.gz**;

Descompactar já movendo pra um diretorio -> **tar -xzvf compactar.tar.gz -C diretório**;

Ver o conteúdo compactado -> **tar -tvf compactado.tar.gz**;

Zip -> **zip -r compactar.zip pasta**

Descompactar zip -> **unzip compactado.zip -d diretorio**;

### Linux: atalhos

**tab** -> autocompleta;

**!!** redigita o comando anterior (cabe concatenação);

**cetinha pra cima** -> volta os comandos;

**Ctrl c** -> cancela comando em execução;

**Ctrl l** -> limpa o terminal (ou o comando clear);

**Ctrl Alt t** -> abre o terminal;

**Ctrl Shift R** -> “pesquisa” de comando já utilizados;

**history** -> mostra o histórico de comandos no terminal;

**Ctrl Shift C** -> copia // **Ctrl Shift V** -> cola;

**ls –help** -> mostra todos os comandos, descrevendo oque eles faz (manual);

**man _comando_** -> mostra como o comando pode ser usado (manual do comando em si);

**Exemplos de Concatenação:** **cd etc && ls** -> **&&** serve para concatenar comandos cd e ls // **ls -la** -> concatenar os comando **ls -l** e **ls-a**;

**pwd _diretorio_** -> mostra todo o caminho de diretórios;

**sudo su** -> entrar no root // **exit** -> sai do root;
