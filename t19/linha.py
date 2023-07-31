class Ponto:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = coord_x
        self.coord_y = coord_y


class Linha:
    def __init__(self, ponto1: Ponto, ponto2: Ponto) -> None:
        self.pontos: tuple[Ponto, Ponto] = (ponto1, ponto2)
