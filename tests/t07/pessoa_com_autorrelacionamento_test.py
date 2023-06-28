from datetime import date
from t07.pessoa_com_autorrelacionamento import Pessoa


def test_atributo_nome() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "_nome")
    assert nova_pessoa._nome is None or isinstance(nova_pessoa._nome, str)


def test_atributo_nascimento() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "_nascimento")
    assert nova_pessoa._nascimento is None \
        or isinstance(nova_pessoa._nascimento, date)


def test_atributo_pai() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "_pai")
    assert nova_pessoa._pai is None or isinstance(nova_pessoa._pai, Pessoa)


def test_atributo_mae() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "_mae")
    assert nova_pessoa._mae is None or isinstance(nova_pessoa._mae, Pessoa)


def test_todos_atributos() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "_nome") \
           and hasattr(nova_pessoa, "_nascimento") \
           and hasattr(nova_pessoa, "_pai") \
           and hasattr(nova_pessoa, "_mae")
