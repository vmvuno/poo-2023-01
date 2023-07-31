from __future__ import annotations
from typing import Union


class Versao:
    def __init__(self,
                 id_versao: str,
                 proximo: Union[None, Revisao]) -> None:
        self.id_versao = id_versao
        self.proximo = proximo


class Revisao(Versao):
    def __init__(self,
                 id_versao: str,
                 proximo: Union[None, Revisao],
                 anterior: Versao) -> None:
        super().__init__(id_versao, proximo)
        self.versao_anterior = anterior


class Software:
    def __init__(self,
                 versoes: list[Versao]) -> None:
        self.versoes = versoes
