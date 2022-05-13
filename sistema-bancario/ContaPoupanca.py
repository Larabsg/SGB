import Conta
class ContaPoupanca(Conta.Conta):
    def __init__(self, nConta, saldo, saque, cpf, nome, senha):
        super().__init__(nConta, saldo, saque, cpf, nome, senha)
        self.__taxa = taxa
    
    def get_taxa(self):
        return self.__taxa

    def set_taxa(self, taxa):
        self.__taxa = taxa
    