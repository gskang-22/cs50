from twttr import shorten

def test_twttr():
    assert shorten("hello") == "hll"
    assert shorten("testing this test") == "tstng ths tst"
    assert shorten("1234?") == "12324?"