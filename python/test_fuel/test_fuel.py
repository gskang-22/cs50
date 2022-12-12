from fuel import convert, gauge
import pytest

def test_convert():
    pytest.raises(ValueError, convert("as/df"))