import Conta

class ContaCorrente(Conta.Conta):
    #De que forma vcs vão representar as contas correntes com cheque especial?
    def __init__(self, nConta, saldo, saque, cpf, nome, senha):
        super().__init__(nConta, saldo, saque, cpf, nome, senha)
       

 
    
