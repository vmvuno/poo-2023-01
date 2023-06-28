from t07.pessoa_com_nome import PessoaComNome as Pessoa
import pytest


@pytest.fixture
def uma_pessoa() -> Pessoa:
    return Pessoa("Fulano")


def test_inicializacao(uma_pessoa: Pessoa) -> None:
    assert uma_pessoa.nome == "Fulano"


def test_read_only(uma_pessoa: Pessoa) -> None:
    with pytest.raises(AttributeError):
        uma_pessoa.nome = "Beltrano"  # type: ignore
