from abc import ABC, abstractmethod

class Autenticavel(ABC):
    
    @abstractmethod
    def autentica(self):
        pass

# autenticaveis = ["gerente", "diretor", "cliente"]
# Autenticavel.register(autenticaveis)