class Profissao:
    pass


class Professor(Profissao):
    pass


class Advogado(Profissao):
    pass


class Padeiro(Profissao):
    pass


class Acougueiro(Profissao):
    pass


class Trabalhador:
    def __init__(self,
                 *profissoes: Profissao) -> None:
        self.profissoes: list[Profissao] = list(profissoes)
