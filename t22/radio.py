from t22.escala import Escala


class Radio:
    def __init__(self,
                 identificacao: str) -> None:
        self.escalas: list[Escala] = []
        self.identificacao = identificacao

    def adicionar_escala(self, escala: Escala) -> None:
        self.escalas.append(escala)

    def remover_escala(self, escala: Escala) -> None:
        self.escalas.remove(escala)
