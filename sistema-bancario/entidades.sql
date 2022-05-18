create database SGB;
use SGB;
CREATE TABLE `conta` (
	`id` SERIAL PRIMARY KEY,
    `nome` VARCHAR(50) NOT NULL,
    `cpf` VARCHAR(30) NOT NULL,
    `senha` VARCHAR(30) NOT NULL,
    `nConta` int UNIQUE NOT NULL, 
    `saldo` DOUBLE NOT NULL
) 