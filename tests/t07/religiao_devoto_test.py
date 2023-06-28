import pytest
from t07.religiao_devoto import Religiao, Devoto


@pytest.fixture
def uma_religiao() -> Religiao:
    return Religiao()


def test_instanciacao_religiao(uma_religiao: Religiao) -> None:
    assert isinstance(uma_religiao, Religiao)


def test_adicionar_devoto(uma_religiao: Religiao) -> None:
    Devoto(uma_religiao)
    assert isinstance(uma_religiao.devotos, set) \
        and len(uma_religiao.devotos) == 1 \
        and isinstance(next(iter(uma_religiao.devotos)), Devoto)


def test_adicionar_mais_devotos(uma_religiao: Religiao) -> None:
    Devoto(uma_religiao)
    Devoto(uma_religiao)
    Devoto(uma_religiao)

    assert len(uma_religiao.devotos) == 3 \
        and False not in [isinstance(d, Devoto) for d in uma_religiao.devotos]
