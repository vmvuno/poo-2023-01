from T07.Prova import Prova


def test_prova_sem_valor() -> None:
    prova = Prova()
    assert prova.num_questoes is None


def test_prova_adiciona_valor() -> None:
    prova = Prova()
    prova.num_questoes = 2
    assert prova.num_questoes == 2


def test_prova_adiciona_valor_invalido() -> None:
    prova = Prova()
    prova.num_questoes = -1
    assert prova.num_questoes is None


def test_prova_adiciona_valor_invalido_apos_valido() -> None:
    prova = Prova()
    prova.num_questoes = 2
    prova.num_questoes = -1
    assert prova.num_questoes == 2
