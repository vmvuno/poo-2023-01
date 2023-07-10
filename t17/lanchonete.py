from typing import Union


class Sanduiche:
    pass


class Bebida:
    pass


class Detalhe:
    def __init__(self,
                 descricao: str,
                 acompanhamento: str) -> None:

        self.descricaos = descricao
        self.acompanhamento = acompanhamento


class Pedido:
    def __init__(self,
                 sanduiche: Union[Sanduiche, None],
                 bebida: Union[Sanduiche, None],
                 *detalhes: Detalhe) -> None:

        self.sanduiche = sanduiche
        self.bebida = bebida
        self.detalhes = detalhes


class Lanchonete:
    def __init__(self,
                 *sanduiches: Sanduiche) -> None:
        self.sanduiches_servidos = list(sanduiches)

    def servir(self, sanduiche: Sanduiche) -> None:
        self.sanduiches_servidos.append(sanduiche)


class Garconete:
    def __init__(self,
                 *pedidos_coletados: list[Pedido]) -> None:
        self.pedidos_coletados = list(pedidos_coletados)
