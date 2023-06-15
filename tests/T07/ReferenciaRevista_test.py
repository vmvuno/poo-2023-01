import inspect
from T07.Referencia import Referencia
from T07.Revista import Revista


def test_herança() -> None:
    assert inspect.isclass(Referencia) \
        and inspect.isclass(Revista) \
        and issubclass(Revista, Referencia)
