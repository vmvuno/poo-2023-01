from __future__ import annotations
from datetime import datetime, date
from typing import Union


class Emprego:
    def __init__(self,
                 empresa: Empresa,
                 salario: float,
                 ) -> None:
        self._empregado: Union[Pessoa, None] = None
        self.empresa: Empresa = empresa
        self.salario: float = salario
        self.inicio: Union[date, None] = None
        self.fim: Union[date, None] = None

    @property
    def empregado(self) -> Union[Pessoa, None]:
        return self._empregado

    def atribuir_empregado(self, empregado: Pessoa, data: date) -> None:
        self._empregado = empregado
        self.inicio = data
        empregado.adicionar_emprego(self)

    def remover_empregado(self, data: date) -> None:
        if isinstance(self.empregado, Pessoa):
            self.empregado.remover_emprego(self)
            self.fim = data

        self._empregado = None


class Pessoa:
    def __init__(self) -> None:
        self._empregos: list[Emprego] = []

    def adicionar_emprego(self, emprego: Emprego) -> None:
        self._empregos.append(emprego)

    def remover_emprego(self, emprego: Emprego) -> None:
        self._empregos.remove(emprego)


class Empresa:
    def __init__(self) -> None:
        self._empregos: list[Emprego] = []

    def criar_emprego(self, salario: float) -> None:
        self._empregos.append(
            Emprego(self, salario)
        )

    def empregar_pessoa(self,
                        emprego: Emprego,
                        pessoa: Pessoa,
                        data_inicio: date = datetime.now().date()) -> None:
        if emprego not in self._empregos:
            raise ValueError('Esse emprego não existe na empresa')

        emprego.atribuir_empregado(pessoa, data_inicio)

    def desempregar_pessoa(self,
                           emprego: Emprego,
                           data_fim: date = datetime.now().date()) -> None:
        if emprego not in self._empregos:
            raise ValueError('Esse emprego não existe na empresa')

        if emprego.empregado is None:
            raise ValueError('Não há pessoa desempenhando essa função')

        emprego.remover_empregado(data_fim)
