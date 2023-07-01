class Ponto:
    def __init__(self, coordenadas: tuple[float, float]) -> None:
        self.x = coordenadas[0]
        self.y = coordenadas[1]

    def transladar(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy


class Circulo:
    def __init__(self, centro: Ponto, raio: float) -> None:
        self.centro = centro
        self.raio = raio

    def transladar(self, dx: float, dy: float) -> None:
        self.centro.transladar(dx, dy)
