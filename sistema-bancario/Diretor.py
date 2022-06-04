import Funcionario
import Autenticavel

class Diretor(Funcionario.Funcionario):
    def __init__(self, nome, cpf, cargo, salario, agencia):
        super().__init__(nome, cpf, cargo, salario, agencia)
    
    def visualizarContas(nAgencia):
        pass

    def cadastrarFuncionarios(self):
        pass

    def visualizarFuncionarios(self):
        pass

    def emprestimoFuncionario(self):
        pass
    
