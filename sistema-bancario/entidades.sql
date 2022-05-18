create database SGB;
use SGB;
CREATE TABLE `conta` (
	`id` SERIAL PRIMARY KEY,
    `nome` VARCHAR(50) NOT NULL,
    `cpf` VARCHAR(30) NOT NULL,
    `senha` VARCHAR(30) NOT NULL,
    `nConta` int UNIQUE NOT NULL, 
    `saldo` DOUBLE NOT NULL
);

-- CREATE TABLE 'transacao' (
--     'id' SERIAL PRIMARY KEY,
--     'nConta' INT NOT NULL,
--     FOREIGN KEY (nConta) REFERENCES conta(nConta)
--     'tipo' VARCHAR(25) NOT NULL,
--     valor DOUBLE NOT NULL
-- );






