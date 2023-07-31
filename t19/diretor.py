class Cargo:
    pass


class Aluno(Cargo):
    pass


class Funcionario(Cargo):
    pass


class Docente(Cargo):
    pass


class Diretor(Docente):
    pass


class ViceDiretor(Docente):
    pass


class Pessoa:
    def __init__(self, cargo: Cargo) -> None:
        self.cargo = cargo
