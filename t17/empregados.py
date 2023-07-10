from __future__ import annotations
from typing import Union


class Funcionario:
    def __init__(self,
                 gerente: Union[None, Funcionario],
                 *gerenciados: Funcionario) -> None:
        self.gerente = gerente
        self._gerenciados = list(gerenciados)

        if self.gerente is not None:
            self.gerente._gerenciados.append(self)
