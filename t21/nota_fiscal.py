from t21.pedido import Pedido
from t21.pagamento import Pagamento


class NotaFiscal:
    def __init__(self,
                 pedidos: list[Pedido],
                 pagamentos: list[Pagamento]):
        self.pedido_discriminado = pedidos
        self.pagamentos_associados = pagamentos
