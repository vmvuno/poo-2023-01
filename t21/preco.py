from enum import Enum


class Moeda(Enum):
    REAL = 0
    PESO = 1
    DOLAR = 2
    EURO = 3


class Preco:
    def __init__(self,
                 valor: float,
                 moeda: Moeda):
        self.valor = valor
        self.moeda = moeda
