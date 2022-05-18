import Conta


class ContaPoupanca(Conta.Conta):
    def __init__(self, nConta, saldo, cpf, nome, senha, taxa):
        super().__init__(nConta, saldo, cpf, nome, senha)
        self.__taxa = taxa

    def get_taxa(self):
        return self.__taxa

    def set_taxa(self, taxa):
        self.__taxa = taxa

    def saldo(self, saldo, taxa):
        saldo = saldo + taxa
        # chamar metodo updateSaldo