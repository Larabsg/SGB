class Funcionario():
    def __init__(self, nome, matricula, cargo):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargo = cargo
    
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        
        