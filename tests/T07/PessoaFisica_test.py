from inspect import isclass
from T07.PessoaAbstrata import PessoaAbstrata
from T07.PessoaFisica import PessoaFisica


def test_pessoa_fisica() -> None:
    assert isclass(PessoaFisica) \
        and issubclass(PessoaFisica, PessoaAbstrata)
