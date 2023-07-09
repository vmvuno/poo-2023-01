from __future__ import annotations
from typing import Union


class Elemento:
    def __init__(self,
                 ancestral: Union[Elemento, None],
                 *descendentes: Elemento) -> None:

        self.ancestral = ancestral
        self.descendentes = list(descendentes)


class Raiz:
    def __init__(self,
                 no_raiz: Elemento):

        self._raiz = no_raiz
        self._raiz.ancestral = None
