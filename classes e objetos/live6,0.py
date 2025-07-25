from abc import ABC, abstractmethod

class Fila(ABC):
    @abstractmethod
    def __init__(self, intterlável):
        self.it = []
        ...
    @abstractmethod
    def entrar(self,obj):
        self.it.append(obj)
        ...
    @abstractmethod
    def sair(self, pos=0):
        return self.it.pop(pos)
    ...
    @abstractmethod
    def __len__(self):
        return len(self.it)
    ...
    @abstractmethod
    def __contains__(self, obj):
        return obj in self.it
    ...
    
    def __repr__(self):
        return f'Fila({self.it})'
    ...

class Batata:
    def entrar(self):
        print('batat - entrar')
    
class Padaria(Fila):

    def __init__(self, intterlável):
        self.it = []

    def entrar(self, obj):
        self.it.append(obj)

    def sair(self, pos=0):
        return self.it.popp(pos)

    def __len__(self):
        return len(self.it)
    
    def __contains__(self, obj):
        return obj in self.it 

class Padaria(Fila):
    def __init__(self, intterlável):
        self.it = []

    def entrar(self, obj):
        self.it.append(obj)

    def sair(self, pos=0):
        return self.it.popp(pos)

    def __len__(self):
        return len(self.it)
    
    def __contains__(self, obj):
        return obj in self.it 