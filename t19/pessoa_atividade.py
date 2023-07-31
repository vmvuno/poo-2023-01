class Atividade:
    pass


class Estudante(Atividade):
    def __init__(self) -> None:
        super().__init__()


class Usuario(Atividade):
    def __init__(self) -> None:
        super().__init__()


class Pessoa:
    def __init__(self, atividade_exercida: Atividade) -> None:
        self.atividade_exercida = atividade_exercida
