import Conta
from connection_sqlite import *


class ContaPoupanca(Conta.Conta):
    def __init__(self, nConta, saldo, cpf, nome, senha, tipoConta, gerente, TemEmprestimo, taxa):
        super().__init__(nConta, saldo, cpf, nome, senha, tipoConta, gerente, TemEmprestimo)
        self.__taxa = taxa

    def get_taxa(self):
        return self.__taxa

    def set_taxa(self, taxa):
        self.__taxa = taxa

    def saldo(self, saldo, taxa):
        saldo = saldo + taxa
        # chamar metodo updateSaldo

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
