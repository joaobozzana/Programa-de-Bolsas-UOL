-- Dimensão
CREATE TABLE Ator (
    id VARCHAR(32) PRIMARY KEY,
    nomeartista VARCHAR(255),
    anonascimento VARCHAR(4),
    anofalecimento VARCHAR(4),
    profissao VARCHAR(32),
    generoartista VARCHAR(10)
);

CREATE TABLE FilmeAtor (
    id_filme VARCHAR(32),
    id_ator VARCHAR(32),
    personagem VARCHAR(64)
    PRIMARY KEY (id_filme, id_ator),
    FOREIGN KEY (id_filme) REFERENCES Filme(id),
    FOREIGN KEY (id_ator) REFERENCES Ator(id)
);

CREATE TABLE Filme (
    id VARCHAR(32) PRIMARY KEY,
    titulooriginal VARCHAR(64),
    tempominutos INT,
    genero VARCHAR(64),
    numerovotos int,
    lancamento DATE,
    avaliacao DOUBLE,
    orcamento BIGINT,
    receita BIGINT
);
