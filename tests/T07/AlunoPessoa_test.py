from T07.Pessoa import Pessoa
from T07.AlunoPessoa import Aluno


def test_aluno_pessoa() -> None:
    assert issubclass(Aluno, Pessoa)
