from datetime import datetime as Data


class Periodo:
    def __init__(self, data_inicio: Data, data_final: Data) -> None:
        self.data_inicial = data_inicio
        self.data_final = data_final
