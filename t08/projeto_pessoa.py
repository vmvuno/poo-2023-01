class Pessoa:
    pass


class Projeto:
    def __init__(self) -> None:
        self._pessoas: set[Pessoa] = set()

    def adicionar_pessoa(self, pessoa: Pessoa) -> None:
        self._pessoas.add(pessoa)

    def remover_pessoa(self, pessoa: Pessoa) -> None:
        self._pessoas.remove(pessoa)
