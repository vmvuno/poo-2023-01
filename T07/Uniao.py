from T07.PessoaComNome import PessoaComNome as Pessoa


class Uniao:
    def __init__(self, pessoa1: Pessoa, pessoa2: Pessoa) -> None:
        self._parceiros: tuple[Pessoa, Pessoa] = (pessoa1, pessoa2)

        self._filhos: set[Pessoa] = set()

    def novo_filho(self, filho: Pessoa) -> None:
        self._filhos.add(filho)

    @property
    def filhos(self) -> set[Pessoa]:
        return self._filhos
