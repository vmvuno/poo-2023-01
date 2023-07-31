from __future__ import annotations


class Presidente:
    def __init__(self) -> None:
        self.ministros_nomeados: list[Ministro] = []

    def nomear_ministro(self, ministro: Ministro) -> None:
        self.ministros_nomeados.append(ministro)


class Ministro:
    def __init__(self) -> None:
        self.assessores_nomeados: list[Assessor] = []

    def nomear_assessor(self, assessor: Assessor) -> None:
        self.assessores_nomeados.append(assessor)


class Assessor:
    pass
