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
<<<<<<< HEAD
            # chamar metodo updateSaldo
=======
            # chamar metodo updateSaldo
    
    
>>>>>>> 2de1d65e2357bf7174ea4c805ae7fe82d7079998
