class Pizza:
    pedaços = 8

    @classmethod
    def mudar_tamanho(cls, pedaços):
        cls.pedaços = pedaços

    @staticmethod
    def ingredientes():
        return 'Ingredientes'

class Marrguerita(Pizza):

    @staticmethod
    def ingredientes():
        return ['queijo', 
                'mussarela',
                'tomate,'
                'manjericão']
    ...
