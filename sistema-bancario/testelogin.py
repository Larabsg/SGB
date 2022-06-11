
from Autenticavel import Autenticavel
from Diretor import Diretor


class SistemaInterno:
    def login(self, obj):
        if (hasattr(obj, 'autentica')):
            
            return "login com sucesso"
        else:
            print('{} não é autenticável'.format(self.__class__.__name__))
            return "login sem sucesso"


if __name__ == '__main__':
    diretor = Diretor('melissa', 1549, 'Diretor', 10000, 1000, 1234)
    sistema = SistemaInterno()
    sistema.login(diretor)