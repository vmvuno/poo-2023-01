from pytest import raises
from T07.Interface import InterfaceProvaFormal, InterfaceProvaFormal2
from T07.ProvaComInterface import ProvaComIdentificacaoPithonico
from T07.ProvaComInterface import ProvaComIdentificacaoConvencional


def test_atributo_nome_pithonico() -> None:
    a = ProvaComIdentificacaoPithonico()
    assert hasattr(a, 'nome') and not callable(a.nome)


def test_valor_atributo_nome_pithonico() -> None:
    a = ProvaComIdentificacaoPithonico()
    assert a.nome is None or isinstance(a.nome, str)


def test_interface_pithonico() -> None:
    assert issubclass(ProvaComIdentificacaoPithonico, InterfaceProvaFormal)


def test_not_interface_pithonico() -> None:
    assert not issubclass(ProvaComIdentificacaoConvencional,
                          InterfaceProvaFormal)


def test_method_get_nome() -> None:
    a = ProvaComIdentificacaoConvencional()
    assert hasattr(a, 'get_nome') and callable(a.get_nome)


def test_valor_atributo_nome_convencional() -> None:
    a = ProvaComIdentificacaoConvencional()
    assert a.get_nome() is None or isinstance(a.get_nome(), str)


def test_interface_convencional() -> None:
    assert issubclass(ProvaComIdentificacaoConvencional,
                      InterfaceProvaFormal2)


def test_not_interface_convencional() -> None:
    assert not issubclass(ProvaComIdentificacaoPithonico,
                          InterfaceProvaFormal2)


def test_falha_interface_convencional() -> None:
    class Incompleta(InterfaceProvaFormal2):
        pass

    with raises(TypeError):
        Incompleta()  # type: ignore


def test_falha_interface_pithonica() -> None:
    class Incompleta(InterfaceProvaFormal):
        pass

    with raises(TypeError):
        Incompleta()  # type: ignore
