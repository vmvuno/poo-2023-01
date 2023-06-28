from t07.pessoa import Pessoa
from t07.aluno_pessoa import Aluno


def test_aluno_pessoa() -> None:
    assert issubclass(Aluno, Pessoa)
