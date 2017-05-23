import random
import string

class Robot(object):
    def __init__(self):
        self.name = self.random_name()

    def reset(self):
        self.name = self.random_name()

    def random_name(self):
        random.seed()
        letters = random.choices(string.ascii_uppercase, k=2)
        digits = random.choices(string.digits, k=3)
        return ''.join(letters) + ''.join(digits)
