from t07.pessoa_com_atributos import Pessoa


def test_atributo_dia() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "_dia")


def test_atributo_mes() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "_mes")


def test_atributo_ano() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "_ano")


def test_atributo_idade() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "idade")


def test_todos_atributos() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "_dia")
    assert hasattr(nova_pessoa, "_mes")
    assert hasattr(nova_pessoa, "_ano")
    assert hasattr(nova_pessoa, "idade")
