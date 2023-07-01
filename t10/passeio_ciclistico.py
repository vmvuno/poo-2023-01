from datetime import datetime
from t10.cliente_ciclista import ClienteCiclista
from t10.pessoa import Sexo


class PasseioCiclistico:
    def __init__(self,
                 data_horario: datetime,
                 faixa_etaria_publico_alvo: tuple[int, int],
                 sexo_publico_alvo: list[Sexo],
                 percurso: list[str]) -> None:

        self._data_horario = data_horario
        self._faixa_etaria_publico_alvo = faixa_etaria_publico_alvo
        self._sexo_publico_alvo = sexo_publico_alvo
        self._percurso = percurso
        self._participantes: list[ClienteCiclista] = []

    def convidar_clientes(self,
                          clientes: list[ClienteCiclista]) -> None:
        idade_minima = min(self._faixa_etaria_publico_alvo)
        idade_maxima = max(self._faixa_etaria_publico_alvo)

        for cliente in clientes:
            if idade_minima <= cliente.idade <= idade_maxima \
                    and cliente.sexo in self._sexo_publico_alvo:
                cliente.receber_convite(self)

    def adicionar_participante(self,
                               participante: ClienteCiclista) -> None:
        if participante not in self._participantes:
            self._participantes.append(participante)

    def __str__(self) -> str:
        ret_str = "Passeio Ciclistico!\n"
        ret_str += f"Data: dia {self._data_horario.strftime('%d/%m/%Y')}, "
        ret_str += f"às {self._data_horario.strftime('%H:%M')}\n"
        ret_str += "Publico alvo: "

        if Sexo.MASCULINO in self._sexo_publico_alvo \
                and Sexo.FEMININO not in self._sexo_publico_alvo:
            ret_str += "Homens"

        elif Sexo.MASCULINO not in self._sexo_publico_alvo \
                and Sexo.FEMININO in self._sexo_publico_alvo:
            ret_str += "Mulheres"

        ret_str += f"de {min(self._faixa_etaria_publico_alvo)} a "
        ret_str += f"{max(self._faixa_etaria_publico_alvo)} anos de idade"

        return ret_str
