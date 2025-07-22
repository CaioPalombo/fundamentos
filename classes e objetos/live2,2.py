class Pizza:
    pedaços = 8 

    def __init__(self, sabor):
        self.sabor = sabor

    def pegar_pedaço(self):          
        #Método de instância
        self.pedaços -= 1

    @classmethod
    def mudar_tamanho(cls, pedaços):
        cls.pedaços = pedaços

    @staticmethod
    def ingredientes():
        return "Massa, molho de tomate, queijo, manjericao "