from __future__ import annotations
from typing import Union


class Elemento:
    def __init__(self,
                 anterior: Union[None, Elemento],
                 proximo: Union[None, Elemento]) -> None:
        self.anterior = anterior
        self.proximo = proximo


class FIFO:
    def __init__(self,
                 primeiro: Union[None, Elemento] = None) -> None:
        self.primeiro: Union[None, Elemento] = primeiro

    def inserir(self, elemento: Elemento) -> None:
        if self.primeiro is None:
            self.primeiro = elemento

        else:
            cursor: Elemento = self.primeiro
            while cursor.proximo is not None:
                cursor = cursor.proximo

            cursor.proximo = elemento
            elemento.anterior = cursor

    def remover(self) -> Union[None, Elemento]:
        return_value = self.primeiro

        if self.primeiro is not None:
            self.primeiro = self.primeiro.proximo

            if self.primeiro is not None:
                self.primeiro.anterior = None

        return return_value
