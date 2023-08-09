from datetime import datetime

from t22.trabalhadores import Funcionario
from t22.centro_vendas import CentroDeVendas
from t22.bilhete import Bilhete


class Venda:
    def __init__(self,
                 funcionario: Funcionario,
                 data: datetime,
                 bilhetes: tuple[Bilhete],
                 centro_de_vendas: CentroDeVendas):

        self.funcionario = funcionario
        self.data = data.date()
        self.hora = data.time()
        self.bilhete = bilhetes
        self.centro_de_vendas = centro_de_vendas

        self.funcionario.registrar_venda(self)
        self.centro_de_vendas.adicionar_venda(self)
