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
        if(chequeEspecial == True):
            saldo = saldo - saque
            # chamar metodo updateSaldo
    def saldo(self, saldo, taxa):
        saldo = saldo + taxa
        # chamar metodo updateSaldo
    
