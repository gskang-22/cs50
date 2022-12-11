from plates import is_valid

def test_not0():
    assert is_valid("CS05") == True

def test_not_middle():
    assert is_valid("CS50P") == False

def test_