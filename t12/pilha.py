from __future__ import annotations
from typing import Union


class Elemento:
    def __init__(self,
                 anterior: Union[None, Elemento] = None) -> None:
        self.anterior = anterior


class Pilha:
    def __init__(self,
                 topo: Union[None, Elemento] = None) -> None:
        self.topo: Union[None, Elemento] = topo

    def inserir(self, elemento: Elemento) -> None:
        elemento.anterior = self.topo
        self.topo = elemento

    def remover(self) -> Union[None, Elemento]:
        return_value = self.topo

        if self.topo is not None:
            self.topo = self.topo.anterior

        return return_value
