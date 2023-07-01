class Sentenca:
    pass


class Paragrafo:
    def __init__(self, sentencas: list[Sentenca]):
        self.sentencas = sentencas


class Texto:
    def __init__(self, paragrafos: list[Paragrafo]):
        self.paragrafos = paragrafos
