from Autenticavel import Autenticavel

class SistemaInterno():
    def login(self, obj):
        if(isinstance(obj, Autenticavel)):
            obj.autentica(obj.getSenha, obj.getMatricula)
            return True
        else:
            print("{} não é autenticável".format(self.__class__.__name__))
            return False