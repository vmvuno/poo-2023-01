class Festa:
    def novo_convidado(self, convidado: str) -> None:
        self.convidados.add(convidado)

    def __init__(self, convidado: str) -> None:
        self.convidados: set = set()
        self.novo_convidado(convidado)
