from enum import Enum
from t13.luzes import Luz


class TiposDePista(Enum):
    AERODROMO = 1
    HELIPONTO = 2
    HELIDECK = 3


class TiposDeSuperficie(Enum):
    ACO = 1  # Aço
    ARE = 2  # Areia
    ARG = 3  # Argila
    ASPH = 4  # Asfalto ou concretro asfáltico
    BAR = 5  # Barro
    GRVL = 6  # Cascalho
    CIN = 7  # Cinza
    CONC = 8  # Concreto
    GRASS = 9  # Grama
    MAC = 10  # Macadame
    MAD = 11  # Madeira
    MTAL = 12  # Metálico
    PAR = 13  # Paralelepípedo
    PIC = 14  # Piçarra
    SAI = 15  # Saibro
    SIL = 16  # Sílica
    TER = 17  # Terra
    TIJ = 18  # Tijolo


class Cabeceira:
    def __init__(self,
                 identificador: str,
                 luzes: list[Luz]) -> None:
        self.identificador = identificador
        self.iluminacao: list[Luz] = luzes


class Pista:
    def __init__(self,
                 tipo: TiposDePista,
                 identificadores: str,
                 superficie: TiposDeSuperficie,
                 comprimento: float,
                 largura: float,
                 cabeceiras: list[Cabeceira],
                 luzes: list[Luz]) -> None:

        self.tipo = tipo
        self.identifidores = identificadores
        self.superficie = superficie
        self.comprimento = comprimento
        self.largura = largura
        self.iluminacao = luzes

        if len(cabeceiras) != 2:
            raise ValueError("Uma pista deve ter, exatamente, duas cabeceiras")

        self.cabeceiras = cabeceiras
