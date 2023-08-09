from t21.trabalhadores import Trabalhador


class Ordem:
    def __init__(self,
                 emitida_por: Trabalhador,
                 executada_por: Trabalhador) -> None:
        self.emitida_por = emitida_por
        self.executada_por = executada_por
