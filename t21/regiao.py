from t21.mesa import Mesa
from t21.trabalhadores import Garcom


class Regiao:
    def __init__(self,
                 mesas: set[Mesa],
                 garcons: set[Garcom]):
        self.mesas = mesas
        self.garcons = garcons
