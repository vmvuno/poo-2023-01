class Carta:
    pass


class ConfiguracaoCartas:
    def __init__(self) -> None:
        self.cartas: list[Carta] = []


class MaoJogador(ConfiguracaoCartas):
    pass


class Jogador:
    def __init__(self) -> None:
        self.maos: list[MaoJogador] = []


class Monte(ConfiguracaoCartas):
    pass


class Rodada:
    def __init__(self,
                 jogador: Jogador,
                 monte: Monte) -> None:
        self.jogador = jogador
        self.monte = monte
