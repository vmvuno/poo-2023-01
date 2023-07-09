from __future__ import annotations


class No:
    def __init__(self) -> None:
        self.arestas: list[Aresta] = []

    def adicionar_aresta(self, aresta: Aresta) -> None:
        self.arestas.append(aresta)


class Aresta:
    def __init__(self, origem: No, destino: No) -> None:
        self.origem = origem
        self.destino = destino

        self.origem.adicionar_aresta(self)


class Grafo:
    def __init__(self, aresta_inicial: Aresta):
        self.uma_aresta = aresta_inicial
