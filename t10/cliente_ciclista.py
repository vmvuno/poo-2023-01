from datetime import date
from t10.pessoa import Sexo, Pessoa
from t10.bicicleta import Bicicleta
from t10.passeio_ciclistico import PasseioCiclistico


class ClienteCiclista(Pessoa):
    def __init__(self,
                 nome: str,
                 data_nascimento: date,
                 sexo: Sexo) -> None:

        super().__init__(nome, data_nascimento, sexo)
        self._bicicletas: list[Bicicleta] = []
        self._eventos: list[PasseioCiclistico] = []
        self._convites: list[PasseioCiclistico] = []

    def adquirir_bicicleta(self, bicicleta: Bicicleta) -> None:
        if bicicleta not in self._bicicletas:
            self._bicicletas.append(bicicleta)
            bicicleta.atribuir_dono(self)

    def receber_convite(self, evento: PasseioCiclistico) -> None:
        self._convites.append(evento)

    def confirmar_presenca(self, evento: PasseioCiclistico) -> None:
        if evento in self._convites:
            self._eventos.append(evento)
            self._convites.remove(evento)
            evento.adicionar_participante(self)
