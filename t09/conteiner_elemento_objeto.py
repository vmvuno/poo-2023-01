class Elemento:
    pass


class Objeto(Elemento):
    pass


class Conteiner(Elemento):
    def __init__(self, conteudo: set[Elemento]) -> None:
        super().__init__()
        self.conteudo = conteudo
