from __future__ import annotations
from typing import Union


class Cadeira:
    def __init__(self) -> None:
        self._dono: Union[None, Pessoa] = None

    def atribuir_dono(self, dono: Pessoa) -> None:
        self._dono = dono

    @property
    def dono(self) -> Union[Pessoa, None]:
        return self._dono


class Pessoa:
    def __init__(self) -> None:
        self._pertences: list[object] = []
