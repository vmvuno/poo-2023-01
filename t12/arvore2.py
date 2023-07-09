from __future__ import annotations
from typing import Union


class Elemento:
    def __init__(self,
                 pai: Union[Elemento, None],
                 *filhos: Elemento) -> None:

        self.pai = pai
        self.filhos = list(filhos)

        if isinstance(pai, Elemento):
            self.irmaos = pai.filhos
            self.irmaos.remove(self)

        else:
            self.irmaos = []

        for filho in self.filhos:
            filho.pai = self
