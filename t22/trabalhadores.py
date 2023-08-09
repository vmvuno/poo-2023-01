from typing import Union

from t22.escala import Escala
from t22.pessoa import Pessoa
from t22.venda import Venda
from t22.ocorrencia import Ocorrencia
from t22.radio import Radio


# Pelo modelo, uma pessoa pode ser associada a um visitante ou trabalhador,
# mas não ficou claro, pelo minicontexto, como a pessoa estaria associada
# a um visitante ou trabalhandor.
# Portanto, julgou-se adequado substituir a associação entre pessoa e visitante
# no modelo por uma relação de herança, visto que um trabalhador é uma pessoa.
class Trabalhador(Pessoa):
    pass


class Policia(Trabalhador):
    pass


class Justica(Trabalhador):
    def __init__(self,
                 ocorrencias_lavradas: list[Ocorrencia]) -> None:
        self.ocorrencias_lavradas = ocorrencias_lavradas

    def lavrar_ocorrencia(self, ocorrencia: Ocorrencia) -> None:
        self.ocorrencias_lavradas.append(ocorrencia)


class Funcionario(Trabalhador):
    def __init__(self,
                 nome: str,
                 radio: Union[Radio, None]) -> None:
        self.nome = nome
        self.escalas: list[Escala] = []
        self.vendas: list[Venda] = []
        self.radio = radio

    def adicionar_escala(self, escala: Escala) -> None:
        self.escalas.append(escala)

    def registrar_venda(self, venda: Venda) -> None:
        self.vendas.append(venda)

    def excluir_venda(self, venda: Venda) -> None:
        self.vendas.remove(venda)

    def receber_radio(self, radio: Radio) -> None:
        if self.radio is not None:
            print("O colaborador já tem um radio")

        else:
            self.radio = radio
