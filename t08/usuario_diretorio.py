from __future__ import annotations

class Usuario:
    def __init__(self) -> None:
        self.diretorios: list[Diretorio] = []

    def criar_diretorio(self, usuarios_autorizados: list[Usuario]) -> None:
        self.diretorios.append(
            Diretorio(dono=self,
                      autorizados_a_usar=usuarios_autorizados)
        )

    def remover_diretorio(self, diretorio: Diretorio):
        if diretorio in self.diretorios:
            self.diretorios.remove(diretorio)

class Diretorio:
    def __init__(self,
                 dono: Usuario,
                 autorizados_a_usar: list[Usuario]) -> None:
        self.dono: Usuario = dono
        self.usuarios_autorizados = autorizados_a_usar
