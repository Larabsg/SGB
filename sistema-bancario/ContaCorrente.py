import Conta
from connection_sqlite import *


class ContaCorrente(Conta.Conta):
    def __init__(self, nConta, saldo, cpf, nome, senha, tipoConta, gerente, TemEmprestimo):
        super().__init__(nConta, saldo, cpf, nome, senha, tipoConta, gerente, TemEmprestimo)
    
    # NÃO ESTÁ FUNCIONANDO ESSE MÉTODO
    def depositarCorrente(self, nConta, valor):
        user_list = []
        cur.execute(f'select * from conta where nConta = {nConta}')

        for x in cur:
            user_list.append(x)
        if user_list.__len__() == 1:
            saldo = user_list[0][5]
          
        taxa = ((saldo*0.10)*-1)
        saldo = (saldo+valor)-taxa
        cur.execute(f'UPDATE conta SET saldo = {saldo} WHERE nConta = {nConta}')
        cur.execute(f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Depósito", {valor});')
        con_sqlite.commit()
        print('Depósito efetuado com sucesso')
        
    def sacar(self, saque, nConta):

        user_list = []
        cur.execute(f'select * from conta where nConta = {nConta}')

        for x in cur:
            user_list.append(x)

        if user_list.__len__() == 1:
            saldo = user_list[0][5]

            if(saque >= saldo):
                
                saldo = (saldo-saque)
                # print(saldo)
                cur.execute(
                    f'UPDATE conta SET saldo = {saldo} where nConta = {nConta}')
                cur.execute(
                    f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Saque", {saque});')
                con_sqlite.commit()
                print("saldo zero")
            else:

                saldo = (saldo - saque)
                cur.execute(
                    f'UPDATE conta SET saldo = {saldo} WHERE nConta = {nConta};')

                cur.execute(
                    f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Saque", {saque});')
                con_sqlite.commit()
                print('Saque efetuado com sucesso')
