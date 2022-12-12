from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("cat / dog")