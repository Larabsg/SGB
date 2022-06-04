import Funcionario
import Autenticavel
from tela_cadastro_funcionarios import janelaCadastrarFuncionario
from connection_sqlite import *

class Diretor(Funcionario.Funcionario):
    def __init__(self, nome, matricula, cargo, salario, agencia, senha):
        super().__init__(nome, matricula, cargo, salario, agencia, senha)
    
    def visualizarContas(nAgencia):
        pass

    def cadastrarFuncionarios(self):
        janelaCadastrarFuncionario()

    def visualizarFuncionarios(self):
        cur.execute(f'select * from funcionario')
        funcionarios = cur.fetchall()
        return funcionarios

    def emprestimoFuncionario(self):
        pass
    
