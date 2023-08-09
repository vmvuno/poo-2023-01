from datetime import datetime

from t22.centro_vendas import CentroDeVendas
from t22.brinquedo import Brinquedo


class Bilhete:
    # Implementação atende o item 5:
    # Alguns bilhetes são universais, outros são específicos e podem
    # ser empregados apenas para um subconjunto de brinquedos

    # No caso dos bilhetes universais, o conjunto de brinquedos aplicáveis
    # é igual ao conjunto de brinquedos disponíveis
    def __init__(self,
                 brinquedos_aplicaveis: set[Brinquedo]):
        self.brinquedos_aplicaveis = brinquedos_aplicaveis

    def contempla(self, brinquedo: Brinquedo) -> bool:
        return brinquedo in self.brinquedos_aplicaveis


class TrocaAPorB:
    def __init__(self,
                 a: Bilhete,
                 b: Bilhete,
                 data: datetime,
                 diferenca: float,
                 centro_de_vendas: CentroDeVendas) -> None:

        self.a = a
        self.b = b
        self.data = data.date()
        self.hora = data.time()
        self.diferenca = diferenca
        self.centro_de_vendas = centro_de_vendas

        self.centro_de_vendas.adicionar_troca(self)
