from webbrowser import get


class Conta():
    def __init__(self,  nConta, saldo,  cpf, nome, senha, tipoConta):
        self.__nConta = nConta
        self.__saldo = saldo
        self.__cpf = cpf
        self.__nome = nome
        self.__senha = senha
        self.__tipoConta = tipoConta

    def get_nConta(self):
        return self.__nConta

    def set_nConta(self, nConta):
        self.__nConta = nConta

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha
    
    def get_tipoConta(self):
        return self.__tipoConta

    def set_tipoConta(self, tipoConta):
        self.__tipoConta = tipoConta

    def depositar(deposito):
        saldo = saldo + deposito
        # update no bd
    
    def extrato():
        pass
        # puxar do bd

    # def deposito(self):
    # def extrato(self):
