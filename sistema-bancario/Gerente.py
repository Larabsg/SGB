import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, cargo, salario, agencia):
        super().__init__(nome, cpf, cargo, salario, agencia)
    
    def criaConta():
        pass
    
    def getContas():
        pass

    def realizaEmprestimo(nConta, taxa):
        pass