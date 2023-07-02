from __future__ import annotations
from typing import Union


class Funcionario:
    def __init__(self) -> None:
        self._empregador: Union[Lanchonete, None] = None
        self._gerencia: Union[Lanchonete, None] = None

    def definir_empregador(self, empregador: Lanchonete) -> None:
        self._empregador = empregador

    def atribuir_gerencia(self, empregador: Lanchonete) -> None:
        self._gerencia = empregador


class Lanchonete:
    def __init__(self,
                 empregados: list[Funcionario],
                 gerente: Union[Funcionario, None] = None) -> None:

        self._empregados = empregados
        self._gerente = gerente

        if isinstance(self._gerente, Funcionario):
            if self._gerente not in self._empregados:
                self._empregados.append(self._gerente)

            self._gerente.atribuir_gerencia(self)

        for empregado in self._empregados:
            empregado.definir_empregador(self)
