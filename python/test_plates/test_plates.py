from plates import is_valid

def test_not0():
    assert is_valid("CS05") == False

def test_not_middle():
    assert is_valid("CS50P") == False

def test_no_numbers():
    assert is_valid("OUTATIME") == False

def test_no_special():
    assert is_valid("PI3.14") == False

def test_true():
    assert is_valid("CS50") == True

def test_first():
    assert is_valid("123P") == False