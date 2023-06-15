from inspect import isclass
from T07.PessoaAbstrata import PessoaAbstrata
from T07.PessoaJuridica import PessoaJuridica


def test_pessoa_juridica() -> None:
    assert isclass(PessoaJuridica) \
        and issubclass(PessoaJuridica, PessoaAbstrata)
