from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar2 = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12


def test_withdraw():
    jar = Jar()
    jar.deposit(20)
    assert jar.size == 20
    jar.withdraw(11)
    assert jar.size == 9