class Item:
    pass


class Pedido:
    def __init__(self, lista_de_pedidos: list[Item] = list()) -> None:
        self.listas_de_pedidos = lista_de_pedidos


class Armazem:
    pass


class Cidade:
    def __init__(self, armazens: set[Armazem] = set()) -> None:
        self.armazens = armazens


class Viagem:
    def __init__(self,
                 itinerario: list[Cidade] = list(),
                 lista_de_pedidos: list[Item] = list()) -> None:
        self.itinerario = itinerario
        self.pedidos = lista_de_pedidos


class CaixeiroViajante:
    def __init__(self, viagens: list[Viagem] = list()):
        self.viagens = viagens
