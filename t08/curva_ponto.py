class Ponto:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self._coords = (x_coord, y_coord)

    @property
    def coords(self) -> tuple[float, float]:
        return self._coords


class Curva:
    def __init__(self, pontos: list[Ponto]) -> None:
        if len(pontos) >= 2:
            self._pontos = pontos

        else:
            raise ValueError('Uma curva deve conter, pelo menos, dois pontos')

    def adicionar_ponto(self, ponto: Ponto) -> None:
        self._pontos.append(ponto)

    def remove_ponto(self, ponto: Ponto) -> None:
        self._pontos.remove(ponto)
