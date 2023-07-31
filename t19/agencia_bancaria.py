from typing import Union


class Cliente:
    pass


class Fila:
    def __init__(self) -> None:
        self.clientes: list[Cliente] = []

    def adicionar_a_fila(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def atender_cliente(self) -> Union[Cliente, None]:
        if len(self.clientes) == 0:
            return None

        atendido = self.clientes[0]
        self.clientes = self.clientes[1:]
        return atendido
