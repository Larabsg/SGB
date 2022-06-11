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

    def realizaEmprestimo(self, nConta, valor, nome):
        user_list = []
        cur.execute(f'select * from conta where nConta = {nConta}')

        for x in cur:
            user_list.append(x)

        if user_list.__len__() == 1:
            saldo = user_list[0][5]

        if saldo < 0:
            taxa = ((saldo*0.5)*-1)
        else:
            taxa = (saldo*0.5)

        saldo = saldo + valor
        valor = valor + taxa
        sql = "UPDATE conta SET saldo = ?, temEmprestimo = ?, gerente = ?, valorEmprestimo = ? WHERE nConta = ?"
        cur.execute(sql, (saldo, True, nome, valor, nConta))

        cur.execute(
            f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Empréstimo", {valor});')
        con_sqlite.commit()
        print('Empréstimo efetuado com sucesso')

        
