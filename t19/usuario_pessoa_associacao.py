class Pessoa:
    pass


class Usuario:
    def __init__(self, pessoa: Pessoa) -> None:
        self.pessoa = pessoa
