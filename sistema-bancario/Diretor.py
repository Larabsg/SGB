import abc
import Funcionario
from tela_cadastro_funcionarios import janelaCadastrarFuncionario
from connection_sqlite import *
from tkinter import messagebox
import tela_inicial_funcionario

class Diretor(Funcionario.Funcionario):
    def __init__(self, nome, matricula, cargo, salario, agencia, senha, nConta):
        super().__init__(nome, matricula, cargo, salario, agencia, senha, nConta)

    def visualizarContas(self, nAgencia):
        cur.execute(f'select * from conta where agencia = {nAgencia}')
        contasByAgencia = cur.fetchall()
        return contasByAgencia

    def cadastrarFuncionarios(self):
        janelaCadastrarFuncionario()

    def visualizarFuncionarios(self):
        cur.execute(f'select * from funcionario')
        funcionarios = cur.fetchall()
        return funcionarios
    
    @abc.abstractmethod
    def autentica(self,senha,matricula):
    
        cur.execute(f"SELECT senha from funcionario where matricula = {matricula}")
        senha_bd = cur.fetchall()
        if senha_bd != []:
            if senha.get() == senha_bd[0][0]:
                tela_inicial_funcionario.janelaEntrarFuncionario(matricula)
        #             # janela.destroy()
            else:
                messagebox.showwarning('', 'Senha inválida! Tente novamente')
        else:
            messagebox.showwarning('', 'Você não pode fazer login no sistema')
    
    def emprestimoFuncionario(self, nConta, valor, nome):

        user_list = []

        cur.execute(f'select * from conta where nConta = {nConta}')

        for x in cur:
            user_list.append(x)
        if user_list.__len__() == 1:
            saldo = user_list[0][5]

            if saldo < 0:
                # Quando o saldo está negativo
                taxa = ((saldo*0.2)*-1)
            else:
                taxa = (saldo*0.2)

            saldo = saldo + valor
            valor = valor + taxa
            sql = "UPDATE conta SET saldo = ?, temEmprestimo = ?, gerente = ?, valorEmprestimo = ? WHERE nConta = ?"
            cur.execute(sql, (saldo, True, nome, valor, nConta))

            cur.execute(
                f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Empréstimo", {valor});')
            con_sqlite.commit()
            print('Empréstimo efetuado com sucesso')
