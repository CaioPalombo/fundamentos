class Pizzaria:
    def __init__(self):
        self._pizzaolo = Pizzaolo()

    def pedido(self, pizza):
        self._pizzaolo.preparar_pizza(pizza)

class forno:
    def __init__(self):
        self.pizza = []
        self.lenha = None

    def assar(self, pizza):
        if not self.lenha:
            print("Não tem lenha no forno")

class Pizzaolo:
    def __init__(self):
        self._forno = forno()

    def preparar_pizza(self, pizza):
        self._forno.assar(pizza)

# O processo que acontece dentro desse código é o sequinte:
# Quando faço um pediso (pizzaria.pedido("Mussarela")), o pizzaolo vai prepará-la
# na class forno, nessa class ele chea se tem lenha no forno e retorna a resposta.
# O cliente não sabe o que está acontecendo na pizzaria, pois o pizzaiolo e o forn
# esrão encpsulados.

        
