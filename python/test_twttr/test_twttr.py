from twttr import shorten

def test_twttr:
    assert shorten("hello") == "hll"
    assert shorten("testing this test") == "tstng ths tst"