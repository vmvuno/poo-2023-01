from t07.pessoa import Pessoa


def test_pessoa() -> None:
    nova_pessoa = Pessoa()
    assert isinstance(nova_pessoa, Pessoa)
