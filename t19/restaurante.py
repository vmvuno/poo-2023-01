from __future__ import annotations
from typing import Union


class Mesa:
    def __init__(self) -> None:
        self.ocupantes: list[Pessoa] = []

    def adicionar_ocupante(self, ocupante: Pessoa) -> None:
        self.ocupantes.append(ocupante)

    def remover_ocupante(self, ocupante: Pessoa) -> None:
        if ocupante in self.ocupantes:
            self.ocupantes.remove(ocupante)


class Pessoa:
    def __init__(self) -> None:
        self.mesa_ocupada: Union[None, Mesa] = None

    def sentar_a_mesa(self, mesa: Mesa) -> None:
        self.mesa_ocupada = mesa
        self.mesa_ocupada.adicionar_ocupante(self)

    def levartar_da_mesa(self) -> None:
        if self.mesa_ocupada is not None:
            self.mesa_ocupada.remover_ocupante(self)
            self.mesa_ocupada = None
