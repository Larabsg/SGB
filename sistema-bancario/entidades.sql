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