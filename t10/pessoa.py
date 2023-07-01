from datetime import date
from enum import Enum


class Sexo(Enum):
    MASCULINO = 0
    FEMININO = 1


class Pessoa:
    def __init__(self,
                 nome: str,
                 data_nascimento: date,
                 sexo: Sexo) -> None:
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._sexo = sexo

    @property
    def idade(self) -> int:
        timedelta = date.today() - self._data_nascimento
        return timedelta.days // 365

    @property
    def sexo(self) -> Sexo:
        return self._sexo
