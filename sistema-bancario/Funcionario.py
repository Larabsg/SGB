class Funcionario():
    def __init__(self, nome, cpf, cargo, salario, agencia):
        self.__nome = nome
        self.__cpf = cpf
        self.__cargo = cargo
        self.__salario = salario
        self.__agencia = agencia

    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf

    def getCargo(self):
        return self.__cargo

    def getSalario(self):
        return self.__salario
    
    def getAgencia(self):
        return self.__agencia
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setCpf(self, cpf):
        self.__cpf = cpf
    
    def setCargo(self, cargo):
        self.__cargo = cargo
    
    def setSalario(self, salario):
        self.__salario = salario
    
    def setAgencia(self, agencia):
        self.__agencia = agencia
