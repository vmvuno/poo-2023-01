from __future__ import annotations
from datetime import datetime
from typing import Union


class Mesa:
    def __init__(self) -> None:
        self.ocupantes: list[
            tuple[Pessoa, datetime, Union[None, datetime]]
            ] = []

    def adicionar_ocupante(self,
                           ocupante: Pessoa,
                           data: datetime) -> tuple[
                               Mesa, datetime, Union[None, datetime]
                               ]:

        self.ocupantes.append((ocupante, data, None))
        return (self, data, None)

    def remover_ocupante(self,
                         ocupante: Pessoa,
                         horario_saida: datetime) -> None:
        for indice, registro in enumerate(self.ocupantes):
            if registro[0] == ocupante and registro[2] is None:
                self.ocupantes[indice] = (registro[0],
                                          registro[1],
                                          horario_saida)


class Pessoa:
    def __init__(self) -> None:
        self.mesas_ocupadas: list[
            tuple[Mesa, datetime, Union[None, datetime]]
            ] = []

    def sentar_a_mesa(self,
                      mesa: Mesa,
                      data: datetime) -> None:
        self.mesas_ocupadas.append(mesa.adicionar_ocupante(self, data))

    def levantar_da_mesa(self, horario_saida: datetime) -> None:
        mesa = self.mesas_ocupadas[-1][0]
        mesa.remover_ocupante(self, horario_saida)
