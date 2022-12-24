from twttr import shorten

def test_twttr():
    assert shorten("HELLO") == "HLL"
    assert shorten("testing this test") == "tstng ths tst"
    assert shorten("1234?") == "1234?"