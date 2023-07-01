from datetime import date
from typing import Union
from t10.pessoa import Pessoa
from t10.mecanico import Mecanico


class Bicicleta:
    def __init__(self,
                 cor: str,
                 comprimento: float,
                 altura: float,
                 aro: int,
                 data_compra: date,
                 periodicidade_revisao: int) -> None:

        self._dono: Union[Pessoa, None] = None
        self._cor = cor
        self._comprimento = comprimento
        self._altura = altura
        self._aro = aro
        self._ultima_revisao = data_compra
        self._periodicade_revisao = periodicidade_revisao
        self._ultimo_mecanico: Union[Mecanico, None] = None

    def pintar(self, nova_cor: str) -> None:
        self._cor = nova_cor

    def trocar_roda(self, novo_aro: int) -> None:
        self._aro = novo_aro

    def anotar_revisao(self, data: date, mecanico: Mecanico) -> None:
        self._ultima_revisao = data
        self._ultimo_mecanico = mecanico

    def atribuir_dono(self, dono: Pessoa) -> None:
        self._dono = dono

    def __str__(self) -> str:
        ret_str = "Descrição da bicicleta\n"
        ret_str += f"Cor: {self._cor}\n"
        ret_str += "Dimensões: \n"
        ret_str += f"    Comprimento: {self._comprimento} cm\n"
        ret_str += f"    Altura:      {self._altura} cm\n\n"

        if self._ultimo_mecanico is not None:
            ret_str += f"Revisada por {self._ultimo_mecanico}, "
            ret_str += f"em {self._ultima_revisao.strftime('%d/%m/%Y')}\n"

        ret_str += f"A ser revisada a cada {self._periodicade_revisao} dia(s)"

        return ret_str
