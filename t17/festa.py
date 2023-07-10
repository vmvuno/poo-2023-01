from __future__ import annotations
from datetime import time
from typing import Union


class Musica:
    pass


class Danca:
    def __init__(self,
                 homem: Pessoa,
                 mulher: Pessoa,
                 hora_inicio: time,
                 hora_fim: time,
                 musica: Musica) -> None:
        self.casal = (homem, mulher)
        self.musica = musica
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim


class Pessoa:
    pass


class Convite:
    def __init__(self,
                 convidado: Pessoa,
                 acompanhante: Union[Pessoa, None]) -> None:

        self.convidado = convidado
        self.acompanhante = acompanhante


class Festa:
    def __init__(self,
                 convites: list[Convite]) -> None:
        self.convites = convites
