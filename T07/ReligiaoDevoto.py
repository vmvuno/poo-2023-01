from __future__ import annotations
from T07.PessoaComAtributos import Pessoa


class Religiao:
    def __init__(self) -> None:
        self._devotos: set[Devoto] = set()

    @property
    def devotos(self) -> set[Devoto]:
        return self._devotos

    def novo_fiel(self, d: Devoto) -> None:
        self._devotos.add(d)


class Devoto(Pessoa):
    def __init__(self, r: Religiao) -> None:
        r.novo_fiel(self)
