class Elemento:
    pass


class Operando(Elemento):
    pass


class Operador(Elemento):
    pass


class Expressao:
    def __init__(self,
                 elementos: list[Elemento]) -> None:
        self.elementos = elementos
