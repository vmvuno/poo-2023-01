import pytest
from T07.Permuta import Permuta


def test_permuta(capsys: pytest.CaptureFixture) -> None:
    p = Permuta("", "abc")
    capture = capsys.readouterr()
    expected_result: str = "abc\nacb\nbac\nbca\ncab\ncba\n"

    assert isinstance(p, Permuta) \
           and capture.out == expected_result
