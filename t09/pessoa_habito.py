class Habito:
    def __init__(self, descricao: str) -> None:
        self._descricao = descricao

    @property
    def descricao(self) -> str:
        return self._descricao


class Pessoa:
    def __init__(self, nome: str, idade: float, habitos: set[Habito]) -> None:
        self.nome = nome
        self.idade = idade
        self.habitos = habitos
