import Conta


class ContaCorrente(Conta.Conta):
    def __init__(self, nConta, saldo, saque, cpf, nome, senha, chequeEspecial):
        super().__init__(nConta, saldo, saque, cpf, nome, senha)
        self.__chequeEspecial = chequeEspecial

    def get_chequeEspecial(self):
        return self.__chequeEspecial

    def set_chequeEspecial(self, chequeEspecial):
        self.__chequeEspecial = chequeEspecial

    def sacar(self, saldo, saque, chequeEspecial):
        if(self.chequeEspecial == True):
            self.saldo -= saque
            # chamar metodo updateSaldo
    
    
