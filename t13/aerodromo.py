import re
from typing import Tuple

from t13.luzes import Luz
from t13.pista import Pista
from t13.servico_comunicacao import ServicoComunicacao


class Aerodromo:
    def __init__(self,
                 codigo_icao: str,
                 nome: str,
                 latitude: float,
                 longitude: float,
                 luzes: list[Luz],
                 pistas: list[Pista],
                 comunicacoes: list[ServicoComunicacao]
                 ) -> None:

        codigo_icao = codigo_icao.upper()
        if not re.fullmatch(r'[A-Z0-9]{4}', codigo_icao):
            raise ValueError('O código ICAO informado não é válido')

        if (latitude < -90) or (latitude > 90):
            raise ValueError('A latitude informada é invalida')

        if (longitude < -180) or (longitude > 180):
            raise ValueError('A longitude informada é invalida')

        self.codigo_icao = codigo_icao
        self.nome = nome
        self.coordenadas: Tuple[float, float] = (latitude, longitude)
        self.iluminacao = luzes
        self.pistas = pistas
        self.comunicacoes = comunicacoes
