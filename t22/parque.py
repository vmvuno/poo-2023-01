from t22.calendario import Calendario
from t22.pessoa import Pessoa
from t22.trabalhadores import Funcionario, Justica, Policia


class Parque:
    def __init__(
            self,
            calendario: Calendario,
            direcao: set[Pessoa],
            diretor: Pessoa,
            colaboradores: set[Funcionario],
            oficiais_justica: set[Justica],
            policiais: set[Policia]
    ) -> None:

        # Novos atributos, que não estavam descritos no diagrama de classes
        # foram adicionados para atender ao item 11 que diz:
        # O parque possui vários colaboradores, todos eles e demais
        # representantes da justiça e da polícia, que não são colaboradores,
        # estão sob a coordenação do diretor do parque.
        self.calendario = calendario
        self.diretor = diretor
        self.direcao = direcao
        self.colaboradores = colaboradores
        self.oficiais_justica = oficiais_justica
        self.policiais = policiais
