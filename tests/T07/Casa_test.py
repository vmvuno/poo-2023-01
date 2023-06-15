import pytest
from T07.Casa import Casa


def test_class_casa(capsys: pytest.CaptureFixture) -> None:
    casa = Casa()
    capture = capsys.readouterr()
    assert isinstance(casa, Casa) and capture.out == "Mais uma casa...\n"
