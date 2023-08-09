from t22.trabalhadores import Trabalhador


class Posto:
    def __init__(self,
                 trabalhadores: set[Trabalhador]):
        self.trabalhadores = trabalhadores
