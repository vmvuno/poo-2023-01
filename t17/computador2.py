from __future__ import annotations
from typing import Any, Union


class CPU:
    def __init__(self) -> None:
        self.cache: list[Any] = []

    def ler_da_memoria(self,
                       memoria: Memoria,
                       endereco: int) -> None:
        self.cache.append(memoria.acessar_endereco(endereco))


class Dispositivo:
    pass


class Teclado(Dispositivo):
    pass


class Mouse(Dispositivo):
    pass


class Memoria(Dispositivo):
    def acessar_endereco(self, endereco: int) -> Any:
        pass


class PlacaMae(Dispositivo):
    def __init__(self, cpus: list[CPU]) -> None:
        self.cpus = cpus


class Computador:
    def __init__(self,
                 *dispositivos: Union[Teclado,
                                      PlacaMae,
                                      Memoria,
                                      Mouse]) -> None:

        self.dispositivos = list(dispositivos)
