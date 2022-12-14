from numb3rs import validate

def test_numbers():
    assert validate("255.0.0.1") == True
    assert validate("512.512.512.512") == False
    assert validate("127.0.0.-1") == False

def test_not_number():
    assert validate("cat") == False