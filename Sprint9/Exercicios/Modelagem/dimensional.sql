-- Demensional de Fatos --

CREATE TABLE locacao (
    idLocacao INT PRIMARY KEY,
    clienteID INT,
    carroID INT,
    vendedorID INT,
    tempoID INT,
    qtdDiaria INT,
    FOREIGN KEY (tempoID) REFERENCES tempo(idTempo),
    FOREIGN KEY (clienteID) REFERENCES cliente(idCliente),
    FOREIGN KEY (carroID) REFERENCES carro(idCarro),
    FOREIGN KEY (VendedorID) REFERENCES vendedor(idVendedor)
);


-- Demensional de Dimensão --

-- Tempo

CREATE TABLE tempo (
    idTempo INT PRIMARY KEY,
    dataLocacao DATE,
    horaLocacao TIME,
    dataEntrega DATE,
    horaEntrega TIME
);

-- Carro
CREATE TABLE carro (
    idCarro INT PRIMARY KEY,
    marca VARCHAR(32),
    modelo VARCHAR(32),
    ano INT,
    chassi VARCHAR(64),
    valorDiaria INT,
    combustivel VARCHAR(32)
);

-- Cliente
CREATE TABLE cliente (
    idCliente INT PRIMARY KEY,
    nome VARCHAR(128),
    cidade VARCHAR(32),
    estado VARCHAR(32),
    pais VARCHAR(32)
);

-- Vendedor
CREATE TABLE vendedor (
    idVendedor INT PRIMARY KEY,
    nome VARCHAR(128),
    sexo INT,
    estado VARCHAR(32)
);