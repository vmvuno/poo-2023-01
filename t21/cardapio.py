from t21.dia_semana import DiaDaSemana
from t21.prato import Prato


class Cardapio:
    def __init__(self,
                 pratos: set[Prato]) -> None:
        self.pratos = pratos

    def pratos_do_dia(self,
                      dia: DiaDaSemana) -> set[Prato]:
        return {
            prato for prato in self.pratos
            if prato.e_servido_no_dia(dia)
        }
