import pytest
from T07.Uniao import Uniao
from T07.PessoaComNome import PessoaComNome as Pessoa


@pytest.fixture
def pessoa1() -> Pessoa:
    return Pessoa("Fulano")


@pytest.fixture
def pessoa2() -> Pessoa:
    return Pessoa("Beltrana")


@pytest.fixture
def filho1() -> Pessoa:
    return Pessoa("Antonia")


@pytest.fixture
def filho2() -> Pessoa:
    return Pessoa("José")


@pytest.fixture
def uma_uniao(pessoa1: Pessoa, pessoa2: Pessoa) -> Uniao:
    return Uniao(pessoa1, pessoa2)


def test_inicializacao(uma_uniao: Uniao,
                       pessoa1: Pessoa,
                       pessoa2: Pessoa) -> None:
    assert isinstance(uma_uniao, Uniao) \
        and uma_uniao._parceiros == (pessoa1, pessoa2) \
        and uma_uniao.filhos == set()


def test_adiciona_filho(uma_uniao: Uniao,
                        filho1: Pessoa,
                        filho2: Pessoa) -> None:
    assert uma_uniao.filhos == set()

    uma_uniao.novo_filho(filho1)
    assert uma_uniao.filhos == {filho1}

    uma_uniao.novo_filho(filho2)
    assert uma_uniao.filhos == {filho1, filho2}
