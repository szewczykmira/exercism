class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, length):
        self.current = 0
        self.start = 0
        self.length = length
        self.clear()

    def change_current(self, elem):
        self.current = (self.current + elem) % self.length

    def change_start(self, elem):
        self.start = (self.start + elem) % self.length

    def empty(self, index):
        self.buffer[index] = None

    def read(self):
        if all([x is None for x in self.buffer]):
            raise BufferEmptyException

        for i in range(self.start, self.start + self.length):
            index = i % self.length
            elem = self.buffer[index]
            if elem is not None:
                self.empty(index)
                self.change_start(1)
                return elem

    def write(self, elem):
        index = (self.current) % self.length
        if self.buffer[index] is not None:
            raise BufferFullException

        self.buffer[index] = elem
        self.change_current(1)

    def clear(self):
        self.buffer = self.length * [None]

    def overwrite(self, elem):
        self.buffer[self.start] = elem
        self.change_start(1)
