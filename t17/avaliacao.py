from __future__ import annotations
from typing import Any


class Questao:
    pass


class Avaliacao:
    def __init__(self,
                 *questoes: Questao) -> None:
        self.questoes = list(questoes)


class Aluno:
    def __init__(self) -> None:
        self.provas: list[Prova] = []

    def adicionar_prova(self, prova: Prova) -> None:
        self.provas.append(prova)


class Resposta:
    pass


class Prova:
    def __init__(self,
                 avaliacao: Avaliacao,
                 aluno: Aluno) -> None:
        self.avaliacao = avaliacao
        self.aluno = aluno
        self.respostas: list[Resposta] = []

    def adicionar_resposta(self,
                           *parametros_resposta: Any) -> None:
        self.respostas.append(
            Resposta(*parametros_resposta)
        )
