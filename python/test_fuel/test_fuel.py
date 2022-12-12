from fuel import convert, gauge

def test_convert():
    pytest.raises(ValueError, convert(fraction))