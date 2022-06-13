create database SGB;
use SGB;
CREATE TABLE `conta` (
	`id` SERIAL PRIMARY KEY,
    `nome` VARCHAR(50) NOT NULL,
    `cpf` VARCHAR(30) NOT NULL,
    `senha` VARCHAR(30) NOT NULL,
    `nConta` int UNIQUE NOT NULL, 
    `saldo` DOUBLE NOT NULL,
    `tipoConta` VARCHAR(30) NOT NULL
) 

CREATE TABLE `funcionario` (
     `id` SERIAL PRIMARY KEY,
     `nome` VARCHAR(100) NOT NULL,
     `matricula` VARCHAR(40) NOT NULL UNIQUE,
     `cargo` VARCHAR(60) NOT NULL
)

CREATE TABLE funcionario(
	id intEGER PRIMARY KEY AUTOINCREMENT,
  	nome VARCHAR(100) NOT NULL,
  	matricula VARCHAR(60) UNIQUE NOT NULL,
  	cargo VARCHAR(60) NOT NULL,
  	senha VARCHAR(60) NOT NULL,
  	salario real not NULL,
  	agencia varchar(15) not NULL,
  	id_nConta int not NULL,
  	FOREIGN KEY(id_nConta) REFERENCES conta(nConta) 	
)

CREATE TABLE data(
  id intEGER PRIMARY KEY AUTOINCREMENT,
  ontem text not NULL,
  hoje text not NULL
)
-- atualizar saldo diaramente quando o tipo de conta for poupança   
CREATE TRIGGER TR_CONTA
AFTER INSERT ON TB_CONTA
BEGIN
    INSERT INTO conta(saldo) values(saldo)
