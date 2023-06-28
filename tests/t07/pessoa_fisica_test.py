from inspect import isclass
from t07.pessoa_abstrata import PessoaAbstrata
from t07.pessoa_fisica import PessoaFisica


def test_pessoa_fisica() -> None:
    assert isclass(PessoaFisica) \
        and issubclass(PessoaFisica, PessoaAbstrata)
