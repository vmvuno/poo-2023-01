class Ponto:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move(self, x_offset: float, y_offset: float) -> None:
        self.x_coord += x_offset
        self.y_coord += y_offset


class Circulo:
    def __init__(self,
                 centro_x: float,
                 centro_y: float,
                 raio: float) -> None:
        self.center = Ponto(centro_x, centro_y)
        self.raio = raio

    def move(self, x_offset: float, y_offset: float) -> None:
        self.center.move(x_offset, y_offset)
