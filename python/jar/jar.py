class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0
    def __str__(self):
        string = "🍪" * self.size
        return f"{string}"

    def deposit(self, n):
        temp = self.size + n
        if temp > self._capacity:
            raise ValueError
        else:
            self.size = temp

    def withdraw(self, n):
        temp = self.size - n
        if temp < 0:
            raise valueError
        else:
            self.size = n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size