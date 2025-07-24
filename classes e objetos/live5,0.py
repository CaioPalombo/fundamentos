'''Implementar um container'''
from collections.abc import Container, Sized, Collection

class Caixa(Collection):
    def __init__(self, seq):
        self.seq = seq
    
    def __contains__(self, other):
        return other in list(self.seq)
        
    def __len__(self):
        return len(self.seq)
    
    def __inter__(self):
        return self

