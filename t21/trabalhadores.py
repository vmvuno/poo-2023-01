from __future__ import annotations
from typing import Union

from t21.pedido import Pedido
from t21.rota import Rota


class Trabalhador:
    def __init__(self,
                 gerente: Union[Trabalhador, None] = None) -> None:
        self.gerente = gerente


class Atendente(Trabalhador):
    def __init__(self) -> None:
        self.pedidos_atendidos: list[Pedido] = []

    def atender_pedido(self, pedido: Pedido) -> None:
        self.pedidos_atendidos.append(pedido)


class Telefonista(Atendente):
    # Atributos e métodos da especialização Telefonista
    pass


class Garcom(Atendente):
    # Atributos e métodos da especialização Garçom
    pass


class Entregador(Trabalhador):
    def __init__(self,
                 rotas: list[Rota] = []) -> None:
        self.rotas = rotas

    def adicionar_rota(self, rota: Rota) -> None:
        self.rotas.append(rota)
