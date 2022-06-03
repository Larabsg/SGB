import Funcionario
from tela_cadastro import janelaCadastrar

class Gerente(Funcionario.Funcionario):
    def __init__(self, nome, cpf, cargo, salario, agencia):
        super().__init__(nome, cpf, cargo, salario, agencia)
    
    def criaConta(self):
        janelaCadastrar()
    
    def getContas(self):
        pass

    def realizaEmprestimo(self):
        pass