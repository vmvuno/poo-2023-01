from datetime import date
from T07.PessoaComTiposClassicos import Pessoa


def test_atributo_nome() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "nome")
    assert nova_pessoa.nome is None or isinstance(nova_pessoa.nome, str)


def test_atributo_nascimento() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "nascimento")
    assert nova_pessoa.nascimento is None \
        or isinstance(nova_pessoa.nascimento, date)


def test_todos_atributos() -> None:
    nova_pessoa = Pessoa()
    assert hasattr(nova_pessoa, "nome") and hasattr(nova_pessoa, "nascimento")
