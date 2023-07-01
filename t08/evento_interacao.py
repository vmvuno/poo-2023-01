from __future__ import annotations


class ElementoDeInteracao:
    pass


class Menu(ElementoDeInteracao):
    pass


class BarraDeRolagem(ElementoDeInteracao):
    pass


class Botao(ElementoDeInteracao):
    pass


class Janela:
    def __init__(self) -> None:
        self.elementos: list[ElementoDeInteracao] = []

    def add_elemento(self,
                     classe_elemento: type[ElementoDeInteracao],
                     ) -> None:
        self.elementos.append(
            classe_elemento()
        )
