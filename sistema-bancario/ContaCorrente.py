import Conta
from connection_sqlite import *

class ContaCorrente(Conta.Conta):
    def __init__(self, nConta, saldo,cpf, nome, senha, saque):
        super().__init__(nConta, saldo, cpf, nome, senha)
        self.__saque = saque

    def sacar(self, saque, nConta):
        if(saque >= saldo):
            # atualiza para zero o saldo 
            # é preciso fazer uma consulata novamente no banco
            cur.execute('UPDATE conta SET saldo = 0')
        else:
            # diminui o saque
            saldo = saldo - saque
    
    
