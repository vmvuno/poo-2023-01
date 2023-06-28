class PessoaComNome:
    # Uma pessoa é inicializada apenas com o nome
    def __init__(self, nome: str) -> None:
        self._nome = nome

    # Normalmente, o nome de uma pessoa não se altera,
    # Não havendo um setter, essa se torna uma propriedade read_only
    @property
    def nome(self) -> str:
        return self._nome
