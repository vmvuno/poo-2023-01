import inspect
from t07.referencia import Referencia
from t07.revista import Revista


def test_herança() -> None:
    assert inspect.isclass(Referencia) \
        and inspect.isclass(Revista) \
        and issubclass(Revista, Referencia)
