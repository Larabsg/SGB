import abc

class Autenticavel(abc.ABC):
    
    def __init__(self, senha):
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

    @abc.abstractmethod
    def autentica(self):
        pass
