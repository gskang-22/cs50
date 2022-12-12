from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("cat / dog")

    with pytest.raises(ZeroDivisionError):
        convert("10 / 0")

    with pytest.raises(ValueError):
        convert("3 / 2")

    assert convert("1 / 2") == "50"

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"