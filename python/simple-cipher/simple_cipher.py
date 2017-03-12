from random import choice
from string import ascii_lowercase

LETTERS = ascii_lowercase

class Caesar:
    CODE = 'd'
    
    def __init__(self):
        self.cipher = Cipher(self.CODE)

    def encode(self, phrase):
        return self.cipher.encode(phrase)

    def decode(self, phrase):
        return self.cipher.decode(phrase)


class Cipher:
    KEY_LENGTH = 100

    def __init__(self, key=None):
        self.key = key or self.generate_key()
        if not self.key_is_valid():
            raise ValueError
        self.mapped_key = [LETTERS.index(x) for x in self.key]

    def _code(self, num, letter, mul=1):
        if letter.isalpha():
            lower_letter = letter.lower()
            index = LETTERS.index(lower_letter) + mul * self.key_value(num)
            return LETTERS[index % 26]
        return ''

    def _encode_letter(self, num, letter):
        return self._code(num, letter)

    def encode(self, phrase):
        return ''.join(self._encode_letter(num, l) 
                for num, l in enumerate(phrase))

    def _decode_letter(self, num, letter):
        return self._code(num, letter, mul=-1)

    def decode(self, phrase):
        return ''.join(self._decode_letter(num, l) 
                for num, l in enumerate(phrase))

    def generate_key(self):
        return ''.join([choice(LETTERS) for _ in range(0, 100)])

    def key_is_valid(self):
        return (self.key.isalpha() and self.key.islower())

    def key_value(self, num):
        key_len = len(self.key)
        return self.mapped_key[num % key_len]

