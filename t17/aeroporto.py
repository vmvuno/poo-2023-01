from __future__ import annotations
from typing import Any, Union
from datetime import datetime


class Piloto:
    pass


class CoPiloto:
    pass


class Comissario:
    pass


class Tripulacao:
    def __init__(self,
                 piloto: list[Piloto],
                 copiloto: list[CoPiloto],
                 comissarios: list[Comissario]) -> None:
        self.piloto = piloto
        self.copiloto = copiloto
        self.comissarios = comissarios
        self.voo: Union[None, Voo] = None

    def atribuir_voo(self, voo: Voo) -> None:
        self.voo = voo


class Lugar:
    def __init__(self, corredor: int, fileira: int) -> None:
        self.corredor = corredor
        self.fileira = fileira
        self.ocupante: Union[None, Passageiro] = None

    def atribuir_ocupante(self, ocupante: Passageiro) -> None:
        self.ocupante = ocupante


class Aviao:
    def __init__(self,
                 n_corredores: int,
                 n_fileiras: int) -> None:
        self.assentos: list[Lugar] = []
        self.voos: list[Voo] = []

        for i in range(1, n_corredores + 1):
            for j in range(1, n_fileiras + 1):
                self.assentos.append(Lugar(i, j))

    def registrar_voo(self, voo: Voo) -> None:
        self.voos.append(voo)


class Passageiro:
    def __init__(self, bilhete: Any, lugar: Lugar) -> None:
        self.bilhete = bilhete

        lugar.atribuir_ocupante(self)


class Voo:
    def __init__(self,
                 tripulacao: Tripulacao,
                 aviao: Aviao) -> None:

        aviao.registrar_voo(self)
        tripulacao.atribuir_voo(self)

        self.aviao = aviao
        self.tripulacao = tripulacao


class Operacao:
    def __init__(self,
                 data: datetime,
                 voos: list[Voo]) -> None:
        self._data = data
        self._voos = voos

    def incluir_voo(self, voo: Voo) -> None:
        self._voos.append(voo)


class Aeroporto:
    def __init__(self, operacoes: list[Operacao]) -> None:
        self._operacoes = operacoes

    def incluir_operacao(self, operacao: Operacao) -> None:
        self._operacoes.append(operacao)
