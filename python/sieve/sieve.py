class Point:
    def __init__(self, index):
        self._value = True
        self._index = index

    def __bool__(self):
        return self._value

    def off(self):
        self._value = False

    @property
    def index(self):
        return self._index


def create_points(n):
    return [Point(i) for i in range(0, n + 1)]


def sieve(num):
    dirty_sieve = create_points(num)
    dirty_sieve[0].off()
    dirty_sieve[1].off()
    for elem in dirty_sieve:
        if elem:
            mul = elem.index * 2
            while mul <= num:
                dirty_sieve[mul].off()
                mul += elem.index
    return [elem.index for elem in dirty_sieve if elem]


