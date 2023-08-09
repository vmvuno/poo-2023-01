from t21.preco import Preco
from t21.dia_semana import DiaDaSemana


class Prato:
    def __init__(self,
                 nome: str,
                 preco: Preco,
                 dias_servidos: set[DiaDaSemana]) -> None:
        self.nome = nome
        self.preco = preco
        self.dias_servidos = dias_servidos

    def e_servido_no_dia(self, dia: DiaDaSemana) -> bool:
        return dia in self.dias_servidos
