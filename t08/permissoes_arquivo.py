from __future__ import annotations


class Usuario:
    pass


class Grupo:
    def __init__(self, usuarios: list[Usuario]) -> None:
        self.usuarios: list[Usuario] = usuarios
        self.permissoes: list[Permissao] = []

    def adiciona_a_permissao(self, permissao: Permissao) -> None:
        self.permissoes.append(permissao)


class Permissao:
    def __init__(self, grupo: Grupo) -> None:
        self.grupo: Grupo = grupo
        grupo.adiciona_a_permissao(self)


class Arquivo:
    def __init__(self, permissoes: list[Permissao]) -> None:
        self.permissoes: list[Permissao] = permissoes
