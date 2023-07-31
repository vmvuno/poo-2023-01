from datetime import datetime


class Evento:
    def __init__(self, dia: datetime, descricao: str) -> None:
        self.dia = dia
        self.descricao = descricao


class Calendario:
    def __init__(self,
                 ano: int,
                 feriados: list[Evento],
                 datas_importantes: list[Evento]) -> None:
        self.ano = ano
        self.feriados = feriados
        self.datas_importantes = datas_importantes
