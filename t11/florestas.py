from __future__ import annotations
from enum import Enum


class TipoFolha(Enum):
    pass


class Folha:
    def __init__(self, tipo: TipoFolha) -> None:
        self._tipo = tipo


class Arvore:
    def __init__(self,
                 n_folhas: int,
                 tipo_folha: TipoFolha) -> None:
        self._folhas: list[Folha] = \
            [Folha(tipo_folha) for i in range(n_folhas)]
