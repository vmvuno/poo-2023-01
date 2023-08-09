from t22.trabalhadores import Funcionario
from t22.radio import Radio


class Escala:
    def __init__(self,
                 radios: set[Radio],
                 funcionarios: set[Funcionario]) -> None:

        self.radios = radios
        self.funcionarios: set[Funcionario] = funcionarios

    def atribuir_radio_a_colaborador(self,
                                     colaborador: Funcionario,
                                     radio: Radio) -> None:
        if colaborador not in self.funcionarios:
            print("O colaborador não está nessa escala")
            return

        if radio not in self.radios:
            print("O rádio não está associado a essa escala")
            return

        colaborador.receber_radio(radio)
