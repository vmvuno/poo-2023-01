class Elemento:
    pass


class Vetor:
    def __init__(self, *args: Elemento) -> None:
        self._vetor: list[Elemento] = list(args)

    def push(self, elemento: Elemento) -> None:
        self._vetor += [elemento, ]

    def __getitem__(self, key: int) -> Elemento:
        return self._vetor[key]
