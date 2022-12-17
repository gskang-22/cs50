from seasons import convert

def test_convert():
    assert convert("2022-12-17") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("") 