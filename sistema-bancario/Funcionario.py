class Funcionario():
    def __init__(self, nome, matricula, cargo, salario, agencia, senha, nConta):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargo = cargo
        self.__salario = salario
        self.__agencia = agencia
        self.__senha = senha
        self.__nConta = nConta

    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getMatricula(self):
        return self.__matricula

    @property
    def getCargo(self):
        return self.__cargo

    @property
    def getSalario(self):
        return self.__salario
    
    @property
    def getAgencia(self):
        return self.__agencia

    @property
    def getSenha(self):
        return self.__senha
    
    @property
    def getnConta(self):
        return self.__nConta
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setmatricula(self, matricula):
        self.__matricula = matricula
    
    def setCargo(self, cargo):
        self.__cargo = cargo
    
    def setSalario(self, salario):
        self.__salario = salario
    
    def setAgencia(self, agencia):
        self.__agencia = agencia

    def setSenha(self, senha):
        self.__senha = senha
