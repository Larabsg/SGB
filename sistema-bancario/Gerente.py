import Funcionario
from tela_cadastro import janelaCadastrar
from connection_sqlite import *

class Gerente(Funcionario.Funcionario):
    def __init__(self, nome, matricula, cargo, salario, agencia, senha):
        super().__init__(nome, matricula, cargo, salario, agencia, senha)
    
    def criaConta(self):
        janelaCadastrar()
    
    def getContas(self):
        cur.execute(f'select * from conta where agencia = {super().getAgencia}')
        contas = cur.fetchall()
        return contas

    def realizaEmprestimo(self):
        pass
