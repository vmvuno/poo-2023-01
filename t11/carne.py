from __future__ import annotations
from datetime import date, timedelta


class Produto:
    def __init__(self) -> None:
        self._presente_em_compras: list[Compra.ItemCompra] = []


class Compra:
    class ItemCompra:
        def __init__(self, produto: Produto, quantidade: int) -> None:
            self._produto = produto
            self._quantidade = quantidade

    def __init__(self) -> None:
        self._itens: list[Compra.ItemCompra] = []

    def adicionar_item(self, produto: Produto, quantidade: int) -> None:
        self._itens.append(
            Compra.ItemCompra(produto, quantidade)
        )


class Prestacao:
    def __init__(self, valor: float, data: date) -> None:
        self.valor = valor
        self.data = data


class Carne:
    def __init__(self, valor_total: float, numero_parcelas: int) -> None:
        self._valor_devido = valor_total
        self._numero_parcelas = numero_parcelas
        self._data_inicio: date = date.today()
        self._parcelas: list[Prestacao] = []

        valor_parcela = valor_total / numero_parcelas

        for i in range(1, numero_parcelas + 1):
            self._parcelas.append(
                Prestacao(valor=valor_parcela,
                          data=date.today() + timedelta(days=30*i))
            )
