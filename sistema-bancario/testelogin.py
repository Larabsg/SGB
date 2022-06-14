
from Autenticavel import Autenticavel
from Diretor import Diretor
from Gerente import Gerente
from SistemaInterno import SistemaInterno

# class SistemaInterno():
#     def login(self, obj):
#         if (hasattr(obj, au)):
            
#             return "login com sucesso"
#         else:
#             print('{} não é autenticável'.format(self.__class__.__name__))
#             return "login sem sucesso"


if __name__ == '__main__':
    Autenticavel.register(Diretor)
    diretor = Diretor('melissa', 1549, 'Diretor', 10000, 1000, 1234)
    gerente = Gerente('lourdes', 147892,'Gerente',7000,1000,2578)
    if (isinstance(diretor, Autenticavel)):
        # diretor.autentica('?')
        sistema = SistemaInterno()
        sistema.login(diretor)
        # sistema.login(gerente)
    else:
        print('Diretor não implementa a interface Autenticavel')
    # print(issubclass(Autenticavel))