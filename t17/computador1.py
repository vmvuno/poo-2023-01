from typing import Any


class Teclado:
    pass


class Mouse:
    pass


class Memoria:
    def acessar_endereco(self, endereco: int) -> Any:
        pass


class CPU:
    def __init__(self) -> None:
        self.cache: list[str] = []

    def requere_dados_da_memoria(self,
                                 memoria: Memoria,
                                 endereco: int) -> None:
        self.cache.append(memoria.acessar_endereco(endereco))


class PlacaMae:
    def __init__(self, processadores: list[CPU]) -> None:
        self.cpus = processadores


class Computador:
    def __init__(self,
                 teclados: list[Teclado],
                 mouses: list[Mouse],
                 placas_mae: list[PlacaMae]) -> None:
        self.teclados = teclados
        self.mouses = mouses
        self.placas_mae = placas_mae
