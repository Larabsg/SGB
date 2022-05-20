class Conta():
    def __init__(self,  nConta, saldo, saque, cpf, nome, senha):
        self.__nConta = nConta
        self.__saldo = saldo
        self.__saque = saque
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

    def get_saque(self):
        return self.__saque

    def set_saque(self, saque):
        self.__saque = saque
    
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

    # METODOS QUE VÃO SER SOBRESCRITOS
    #Precisa mesmo passar o saldo? O próprio objeto já não tem esse valor?
    def sacar(self, saldo, saque):
    
    def extrato(self):
        
        
    # def saque(self):
    # def deposito(self):
    # def extrato(self):
        
