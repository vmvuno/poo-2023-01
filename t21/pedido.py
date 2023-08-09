from datetime import datetime
from typing import Union

from t21.prato import Prato
from t21.bebida import Bebida
from t21.trabalhadores import Atendente
from t21.mesa import Mesa
from t21.domicilio import Domicilio
from t21.cliente import Cliente


class ItemPedido():
    def __init__(self,
                 item: Union[Prato, Bebida],
                 quantidade: int,
                 devolvido: bool,
                 observacao: str) -> None:
        self.item = item
        self.quantidade = quantidade
        self.devolvido = devolvido
        self.observacao = observacao


class Pedido:
    def __init__(self,
                 data: datetime,
                 data_entrega: datetime,
                 clientes: list[Cliente],
                 atendente: Atendente,
                 destino: Union[Mesa, Domicilio]) -> None:

        self.data = data
        self.data_entrega = data_entrega
        self.clientes = clientes
        self.atendente = atendente
        self.destino = destino
        self.itens: list[ItemPedido] = []

        self.atendente.atender_pedido(self)

    def incluir_item(self,
                     item: Union[Prato, Bebida],
                     quantidade: int,
                     devolvido: bool,
                     observacao: str
                     ) -> None:
        self.itens.append(
            ItemPedido(item, quantidade, devolvido, observacao)
        )
