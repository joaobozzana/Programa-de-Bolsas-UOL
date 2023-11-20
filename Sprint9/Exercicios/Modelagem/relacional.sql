-- Tabela Cliente
CREATE TABLE cliente (
    idCliente INT PRIMARY KEY,
    nome VARCHAR(128),
    cidade VARCHAR(32),
    estado VARCHAR(32),
    pais VARCHAR(32)
);

-- Tabela Carro
CREATE TABLE carro (
    idCarro INT PRIMARY KEY,
    marca VARCHAR(32),
    modelo VARCHAR(32),
    ano INT,
    chassi VARCHAR(64),
    valorDiaria INT,
    combustivel VARCHAR(32)
);

-- Tabela Vendedor
CREATE TABLE vendedor (
    idVendedor INT PRIMARY KEY,
    nome VARCHAR(128),
    sexo INT,
    estado VARCHAR(32)
);

-- Tabela Locacao
CREATE TABLE locacao (
    idLocacao INT PRIMARY KEY,
    clienteID INT,
    carroID INT,
    vendedorID INT,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INT,
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (clienteID) REFERENCES cliente(idCliente),
    FOREIGN KEY (carroID) REFERENCES carro(idCarro),
    FOREIGN KEY (VendedorID) REFERENCES vendedor(idVendedor)
);
