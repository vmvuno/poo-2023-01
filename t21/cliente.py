from datetime import datetime
from typing import Union
from t21.pessoa import Pessoa
from t21.mesa import Mesa


class Cliente:
    def __init__(self,
                 pessoas: set[Pessoa],
                 entrada: datetime,
                 saida: datetime) -> None:
        self.pessoas = pessoas
        self.entrada = entrada
        self.saida = saida
        self.mesa: Union[Mesa, None] = None

    def ocupar_mesa(self, mesa: Mesa) -> None:
        self.mesa = mesa

    def desocupar_mesa(self) -> None:
        self.mesa = None
