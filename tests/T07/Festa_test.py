import pytest
from T07.Festa import Festa


@pytest.fixture
def minha_festa() -> Festa:
    return Festa("Fulano")


def test_classe(minha_festa: Festa) -> None:
    assert isinstance(minha_festa, Festa)


def test_atributo(minha_festa: Festa) -> None:
    assert hasattr(minha_festa, "convidados") \
        and isinstance(minha_festa.convidados, set)


def test_inicializacao(minha_festa: Festa) -> None:
    assert minha_festa.convidados == {"Fulano"}


def test_adicionar_convidado(minha_festa: Festa) -> None:
    minha_festa.novo_convidado("Beltrano")
    esperado = {"Fulano", "Beltrano"}
    atual = minha_festa.convidados

    assert esperado == atual
