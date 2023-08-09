from t21.cliente import Cliente


class Mesa:
    def __init__(self,
                 clientes: set[Cliente]) -> None:
        self.clientes = clientes

    def adicionar_cliente(self, cliente: Cliente) -> None:
        self.clientes.add(cliente)
        cliente.ocupar_mesa(self)

    def remover_cliente(self, cliente: Cliente) -> None:
        if cliente in self.clientes:
            self.clientes.remove(cliente)
            cliente.desocupar_mesa()
