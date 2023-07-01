from __future__ import annotations
from typing import Union


class Cidade:
    def __init__(self, nome: str,
                 pais: Union[Pais, None] = None) -> None:
        self._nome = nome
        self._pais = pais

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def pais(self) -> Union[Pais, None]:
        return self._pais

    @pais.setter
    def pais(self, value: Pais) -> None:
        self._pais = value

    def __str__(self) -> str:
        return self._nome


class Pais:
    def __init__(self, nome: str,
                 capital: Cidade,
                 cidades: list[Cidade]) -> None:
        self._nome = nome
        self._capital = capital
        self._cidades = cidades
        self._update_cidades()

    def _update_cidades(self) -> None:
        for cidade in self._cidades:
            cidade.pais = self

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def capital(self) -> str:
        return str(self._capital)
