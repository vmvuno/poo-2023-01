class Circulo:
    def __init__(self, coordenadas: tuple[float, float], raio: float) -> None:
        self.x = coordenadas[0]
        self.y = coordenadas[1]
        self.raio = raio

    def transladar(self, dx: float = 0, dy: float = 0) -> None:
        self.x += dx
        self.y += dy
