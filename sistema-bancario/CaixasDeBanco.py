import Funcionario

class CaixasDeBanco(Funcionario.Funcionario):
    def __init__(self, nome, matricula, cargo, salario, agencia, senha):
        super().__init__(nome, matricula, cargo, salario, agencia, senha)