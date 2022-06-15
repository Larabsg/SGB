import datetime
import time
import schedule

import tela_incial

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
            tela_incial.janelaEntrar(nConta)
            print('Saque efetuado com sucesso')

    # def atualizarSaldo(self):

    #     def job():
    #         cur.execute(
    #             f'UPDATE conta SET saldo = (saldo + 0.05) WHERE tipoConta="Poupança";')
    #         con_sqlite.commit()

    #     # schedule.every().day.at("00:30").do(job)
    #     schedule.every().day.at("00:30").do(job)

    #     while True:
    #         schedule.run_pending()
    #         time.sleep(1)
