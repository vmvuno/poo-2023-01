from inspect import isclass
from pytest import fixture
from t07.pessoas_com_heranca import Pessoa, PessoaFisica, PessoaJuridica


@fixture
def uma_pessoa_fisica() -> PessoaFisica:
    return PessoaFisica(
        nome="Fulano",
        endereco="Rua dos bobos, n.0",
        cpf="000.000.000-00",
        cor_pele="indefinido"
    )


@fixture
def uma_pessoa_juridica() -> PessoaJuridica:
    return PessoaJuridica(
        nome="Nome da empresa",
        endereco="um endereco qualquer",
        cnpj="00.000.000/0001-32",
        nome_fantasia="nome fantasia da empresa"
    )


def test_heranca_pessoa_fisica() -> None:
    assert isclass(PessoaFisica) \
        and issubclass(PessoaFisica, Pessoa)


def test_heranca_pessoa_juridica() -> None:
    assert isclass(PessoaJuridica) \
        and issubclass(PessoaJuridica, Pessoa)


def test_atributos_pessoa_fisica(uma_pessoa_fisica: PessoaFisica) -> None:
    assert hasattr(uma_pessoa_fisica, 'nome') \
        and hasattr(uma_pessoa_fisica, 'endereco') \
        and hasattr(uma_pessoa_fisica, 'cpf') \
        and hasattr(uma_pessoa_fisica, 'cor_pele')


def test_atributos_pessoa_juridica(
        uma_pessoa_juridica: PessoaJuridica
        ) -> None:
    assert hasattr(uma_pessoa_juridica, 'nome') \
        and hasattr(uma_pessoa_juridica, 'endereco') \
        and hasattr(uma_pessoa_juridica, 'cnpj') \
        and hasattr(uma_pessoa_juridica, 'nome_fantasia')
