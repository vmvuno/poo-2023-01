from enum import Enum


class TipoComunicacao(Enum):
    ATIS = 1  # Serviço Automatico de Informação Terminal
    AFIS = 2  # Serviço de Informação de Aeródromo
    DEL = 3  # Autorização de Tráfego
    GND = 4  # Solo
    TWR = 5  # Torre
    APP = 6  # Aproximação
    CTR = 7  # Centro


class ServicoComunicacao:
    def __init__(self,
                 tipo: TipoComunicacao,
                 indicativo_chamada: str,
                 nome_organizacao: str,
                 *frequencias: list[float],
                 ) -> None:

        self.tipo = tipo
        self.indicativo_chamada = indicativo_chamada
        self.frequencias = frequencias
        self.nome_organizacao_prestador = nome_organizacao
