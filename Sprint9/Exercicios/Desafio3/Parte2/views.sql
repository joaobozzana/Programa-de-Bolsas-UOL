-- Dimensão
CREATE TABLE Ator (
    id VARCHAR(32) PRIMARY KEY,
    nome VARCHAR(255),
    anonascimento VARCHAR(4),
    anofalecimento VARCHAR(4),
    profissao VARCHAR(32)
);

-- Dimensão
CREATE TABLE Filme (
    id VARCHAR(10) PRIMARY KEY,
    titulooriginal VARCHAR(64),
    tempominutos INT,
    genero VARCHAR(64)
);

-- Dimensão
CREATE TABLE Tempo (
    lancamento DATE PRIMARY KEY
);

-- Dimensão
CREATE TABLE Avaliacao (
    id INT PRIMARY KEY,
    avaliacao DOUBLE,
    numerovotos int
);

-- Dimensão
CREATE TABLE Financeiro (
    id INT PRIMARY KEY,
    orcamento BIGINT,
    receita BIGINT
);

-- Fato
CREATE TABLE FatoFilmeDetalhes (
    id_tempo VARCHAR(4),
    id_avaliacao INT,
    id_financeiro INT,
    id_filme VARCHAR(10),
    id_ator VARCHAR(10),
    PRIMARY KEY (id_tempo, id_avaliacao, id_Financeiro, id_filme, id_ator),
    FOREIGN KEY (id_tempo) REFERENCES Tempo(lancamento),
    FOREIGN KEY (id_avaliacao) REFERENCES Avaliacao(id),
    FOREIGN KEY (id_financeiro) REFERENCES Financeiro(id),
    FOREIGN KEY (id_filme) REFERENCES Filme(id),
    FOREIGN KEY (id_ator) REFERENCES Ator(id)
);
