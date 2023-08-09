from t22.venda import Venda
from t22.bilhete import TrocaAPorB


class CentroDeVendas:
    def __init__(self,
                 vendas: list[Venda],
                 trocas: list[TrocaAPorB]) -> None:

        self.vendas = vendas
        self.trocas = trocas

    def adicionar_venda(self, venda: Venda) -> None:
        self.vendas.append(venda)

    def excluir_venda(self, venda: Venda) -> None:
        self.vendas.remove(venda)

    def adicionar_troca(self, troca: TrocaAPorB) -> None:
        self.trocas.append(troca)

    def excluir_troca(self, troca: TrocaAPorB) -> None:
        self.trocas.remove(troca)
