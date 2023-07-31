class Ponto:
    def __init__(self, coord_x: int, coord_y: int) -> None:
        self.coord_x = coord_x
        self.coord_y = coord_y


class Cor:
    def __init__(self, vermelho: int, verde: int, azul: int) -> None:
        self.red = vermelho
        self.green = verde
        self.blue = azul


class Pixel:
    def __init__(self,
                 coord_x: int, coord_y: int,
                 vermelho: int, verde: int, azul: int
                 ) -> None:
        self.ponto = Ponto(coord_x, coord_y)
        self.cor = Cor(vermelho, verde, azul)


class Imagem:
    def __init__(
            self,
            informacoes_pixels: list[tuple[int, int, int, int, int]]
            ) -> None:
        self.pixels: list[Pixel] = []
        for informacao in informacoes_pixels:
            self.pixels.append(
                Pixel(
                    coord_x=informacao[0],
                    coord_y=informacao[1],
                    vermelho=informacao[2],
                    verde=informacao[3],
                    azul=informacao[4]
                )
            )
