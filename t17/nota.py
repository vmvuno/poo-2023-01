class Produto:
    pass


class Item:
    def __init__(self,
                 produto: Produto,
                 quantidade: int,
                 preco_unitario: float) -> None:

        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario


class NotaFiscal:
    def __init__(self) -> None:
        self.itens: list[Item] = []

    def adicionar_item(self,
                       produto: Produto,
                       preco_unitario: float,
                       quantidade: int) -> None:
        self.itens.append(
            Item(produto, quantidade, preco_unitario)
        )
