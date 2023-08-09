from t21.trabalhadores import Entregador
from t21.domicilio import Domicilio


class Rota:
    def __init__(self,
                 entregador: Entregador,
                 domicilios: list[Domicilio]) -> None:
        self.entregador = entregador
        self.entregador.adicionar_rota(self)
        self.domicilios = domicilios
