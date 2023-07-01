from datetime import date
from t10.pessoa import Pessoa, Sexo
from t10.bicicleta import Bicicleta


class Mecanico(Pessoa):
    def __init__(self,
                 nome: str,
                 data_nascimento: date,
                 sexo: Sexo) -> None:

        super().__init__(nome, data_nascimento, sexo)

    def revisar_bicicleta(self,
                          bicicleta: Bicicleta,
                          data: date = date.today()) -> None:
        bicicleta.anotar_revisao(data,
                                 mecanico=self)
