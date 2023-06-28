from inspect import isclass
from t07.pessoa_abstrata import PessoaAbstrata
from t07.pessoa_juridica import PessoaJuridica


def test_pessoa_juridica() -> None:
    assert isclass(PessoaJuridica) \
        and issubclass(PessoaJuridica, PessoaAbstrata)
