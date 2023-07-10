from __future__ import annotations
from typing import Union


class Pessoa:
    def __init__(self,
                 automoveis: list[Automovel]) -> None:
        self.dirige = automoveis


class Automovel:
    def __init__(self,
                 marca: str,
                 modelo: str,
                 ano: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motorista: Union[Pessoa, None] = None

    def atribuir_motorista(self,
                           motorista: Union[Pessoa, None]) -> None:
        self.motorista = motorista
