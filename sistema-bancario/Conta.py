class Conta():
    def __init__(self,  nConta, saldo,  cpf, nome, senha):
        self.__nConta = nConta
        self.__saldo = saldo
        self.__cpf = cpf
        self.__nome = nome
        self.__senha = senha

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

    # def saque(self):
    # def deposito(self):
    # def extrato(self):
