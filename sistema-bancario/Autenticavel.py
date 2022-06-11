from abc import ABC, abstractmethod

class Autenticavel():
    def __init__(self, senha):
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

    # @abstractmethod
    def autentica(self):
        #verifica se a senha está correta
        pass

# autenticaveis = ["gerente", "diretor", "cliente"]
# Autenticavel.register(autenticaveis)