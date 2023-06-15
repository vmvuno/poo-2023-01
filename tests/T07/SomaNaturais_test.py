from T07.TestaSomaNaturais import soma_naturais


def test_soma1() -> None:
    assert soma_naturais(1) == 1


def test_soma2() -> None:
    assert soma_naturais(2) == 3


def test_soma3() -> None:
    assert soma_naturais(3) == 6
