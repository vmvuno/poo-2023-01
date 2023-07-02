class Letra:
    def __init__(self, valor: str) -> None:
        self.valor = valor


class Palavra:
    def __init__(self, *sequencia_de_letras: str) -> None:
        if len(sequencia_de_letras) == 0:
            raise ValueError('Uma palavra deve conter, pelo menos, uma letra')

        self._letras: list[str] = list(sequencia_de_letras)


class Frase:
    def __init__(self, *sequencia_de_palavras: Palavra) -> None:
        if len(sequencia_de_palavras) == 0:
            raise ValueError('Uma frase deve conter, pelo menos, uma palavra')

        self._palavras: list[Palavra] = list(sequencia_de_palavras)
