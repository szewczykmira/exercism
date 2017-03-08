class Luhn:
    def __init__(self, number):
        self.array = [int(i) for i in str(number)]

    def addend(self, num, value):
        if num % 2 == 0:
            return value
        value *= 2
        if value > 9:
            return value - 9
        return value

    def addends(self):
        return [self.addend(num, elem) for num, elem in enumerate(
            self.array[::-1])]

    def checksum(self):
        new_array = self.addends()
        return sum(new_array)

    def is_valid(self):
        check_value = self.checksum() % 10
        return check_value == 0

    @classmethod
    def create(cls, number):
        return number
