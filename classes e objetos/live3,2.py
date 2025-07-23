class Pássaro:
    def __init__(self):
        self.nome = nome 

class Urubu(Pássaro):
    def __init__(self, nome, numero):
        super().__init__(nome)
        self.numero = numero

    def __str__(self):
        return f'Urubu(nome="{self.nome}", numero="{self.numero}")'