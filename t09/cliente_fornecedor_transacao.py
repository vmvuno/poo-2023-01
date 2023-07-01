from __future__ import annotations


class Cliente:
    def __init__(self, transacoes: list[Transacao] = []) -> None:
        self.transacoes = transacoes


class Fornecedor:
    def __init__(self, transacoes: list[Transacao] = []) -> None:
        self.transacoes = transacoes


class Transacao:
    def __init__(self, cliente: Cliente, fornecedor: Fornecedor) -> None:
        self.cliente = cliente
        self.fornecedor = fornecedor

        self.cliente.transacoes.append(self)
        self.fornecedor.transacoes.append(self)
