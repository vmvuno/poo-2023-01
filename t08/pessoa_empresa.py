from __future__ import annotations


class Pessoa:
    def __init__(self) -> None:
        self._empregadores: list[Empresa] = []

    @property
    def empregadores(self) -> list[Empresa]:
        return self._empregadores

    def adicionar_empregador(self, empregador: Empresa) -> None:
        self._empregadores.append(empregador)

    def remover_empregador(self, empregador: Empresa) -> None:
        if empregador in self._empregadores:
            self._empregadores.remove(empregador)


class Empresa:
    def __init__(self) -> None:
        self._empregados: list[Pessoa] = []

    @property
    def empregados(self) -> list[Pessoa]:
        return self._empregados

    def empregar_pessoa(self, pessoa: Pessoa) -> None:
        self._empregados.append(pessoa)
        pessoa.adicionar_empregador(self)

    def demitir_pessoa(self, pessoa: Pessoa) -> None:
        if pessoa in self._empregados:
            pessoa.remover_empregador(self)
            self._empregados.remove(pessoa)
