from __future__ import annotations


class Pessoa:
    def __init__(self,
                 *comites: Comite) -> None:
        self.comites = list(comites)

    def adicionar_comite(self, comite: Comite) -> None:
        self.comites.append(comite)


class Comite:
    def __init__(self,
                 presidencia: list[Pessoa],
                 membros: list[Pessoa]) -> None:

        self.presidencia = presidencia
        self.membros = membros

    def adicionar_membro(self, membro: Pessoa) -> None:
        self.membros.append(membro)
        membro.adicionar_comite(self)
