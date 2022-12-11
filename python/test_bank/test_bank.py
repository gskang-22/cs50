from bank import value

def test_0():
    assert value("hello there") == 0

def test_20():
    assert value("how are you?") == 20

def test_100():
    assert value("asdf") == 100