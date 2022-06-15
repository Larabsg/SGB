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

CREATE TRIGGER tr_conta AFTER INSERT ON conta
  BEGIN 
    UPDATE conta SET saldo = (saldo * 0.9) WHERE tipoconta = (SELECT * FROM conta WHERE tipoConta = 'Poupança');
  END;
  
-- CREATE OR REPLACE FUNCTION saldo_atualizado() RETURNS TRIGGER AS $saldo_atual$
--     BEGIN
--         IF (TG_OP = 'INSERT') THEN
-- 			UPDATE conta SET saldo = (saldo * 1.0023) FROM extrato e WHERE e.idconta = numero AND operacao = '013' AND e.datahora_Atualiza != current_date;
-- 		END IF;
-- 		RETURN NEW;
--     END;
-- $saldo_atual$ LANGUAGE plpgsql;

-- CREATE TRIGGER saldo_atual BEFORE INSERT OR UPDATE ON extrato
--     FOR EACH ROW EXECUTE FUNCTION saldo_atualizado();


-- CREATE OR REPLACE FUNCTION data_atualizado() RETURNS TRIGGER AS $data_atual$
--     BEGIN
--         IF (TG_OP = 'INSERT') THEN
-- 			UPDATE extrato SET datahora_Atualiza = current_date FROM conta co WHERE idconta = co.numero AND co.operacao = '013';
-- 		END IF;
-- 		RETURN NEW;
--     END;
-- $data_atual$ LANGUAGE plpgsql;

-- CREATE TRIGGER data_atual AFTER INSERT OR UPDATE ON extrato
--     FOR EACH ROW EXECUTE FUNCTION data_atualizado();