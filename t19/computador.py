from __future__ import annotations
from typing import Union


class Computador:
    def __init__(self) -> None:
        self.aluno: list[Aluno] = []

    def atribuir_a_aluno(self, aluno: Aluno) -> None:
        self.aluno.append(aluno)

    def remover_atribuicao(self, aluno: Aluno) -> None:
        self.aluno.remove(aluno)


class Aluno:
    def __init__(self) -> None:
        self.UFG: Union[Computador, None] = None
        self.casa: list[Computador] = []

    def atribuir_computador_ufg(self, computador: Computador) -> None:
        self.UFG = computador
        computador.atribuir_a_aluno(self)

    def remover_computador_ufg(self) -> None:
        if self.UFG is not None:
            self.UFG.remover_atribuicao(self)
            self.UFG = None

    def atribuir_computador_domestico(self, computador: Computador) -> None:
        self.casa.append(computador)
        computador.atribuir_a_aluno(self)

    def remover_computador_domestico(self, computador: Computador) -> None:
        computador.remover_atribuicao(self)
        self.casa.remove(computador)
