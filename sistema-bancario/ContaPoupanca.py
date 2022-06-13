import datetime

import Conta
from connection_sqlite import *


class ContaPoupanca(Conta.Conta):
    def __init__(self, nConta, saldo, cpf, nome, senha, tipoConta, gerente, TemEmprestimo):
        super().__init__(nConta, saldo, cpf, nome, senha, tipoConta, gerente, TemEmprestimo)

    def sacar(self, saque, nConta):
        user_list = []
        cur.execute(f'select * from conta where nConta = {nConta}')

        for x in cur:
            user_list.append(x)

        if user_list.__len__() == 1:
            saldo = user_list[0][5]

            saldo = (saldo - saque)
            cur.execute(
                f'UPDATE conta SET saldo = {saldo} WHERE nConta = {nConta};')

            cur.execute(
                f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Saque", {saque});')
            con_sqlite.commit()
            print('Saque efetuado com sucesso')

    def atualizarData(self):
        
        ontem = datetime.date.today() - datetime.timedelta(1)
        print(ontem)
        cur.execute(f'UPDATE data SET ontem={ontem}')
        con_sqlite.commit()

    def atualizarSaldo(self, nConta):
        
        hoje = datetime.date.today()
        
        user_list = []
        cur.execute(f'select * from conta where nConta = {nConta} ')

        for x in cur:
            user_list.append(x)

        if user_list.__len__() == 1:
            saldo = user_list[0][5]

        saldo = (saldo + 0.5)
        
        cur.execute(f'SELECT ontem FROM data')
        ontem = cur.fetchall()
        
        # mudar logica
        if ontem[0][0] != hoje:
            cur.execute(f'UPDATE conta SET saldo={saldo} WHERE nConta = {nConta}')
            con_sqlite.commit()
