from um import count

def test_1():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("um?") == 1

def test_2():
    assert count("Um, thanks, um...") == 2

def test_in_word():
    assert count("Um, thanks for the album.") == 1