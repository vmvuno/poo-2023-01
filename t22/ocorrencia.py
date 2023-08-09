from datetime import datetime

from t22.pessoa import Pessoa


class Ocorrencia:
    def __init__(
            self,
            pessoas_envolvidas: set[Pessoa],
            local: str,
            data: datetime,
            descricao: str
            ) -> None:

        # Adições realizadas para atender ao requisito 10
        # Cada ocorrência está associada a um local e instante de tempo,
        # além de uma descrição contendo detalhes do ocorrido
        self.pessoas_envolvida = pessoas_envolvidas
        self.local = local
        self.data = data
        self.descricao = descricao
