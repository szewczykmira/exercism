import string


LETTERS = string.ascii_lowercase


def code(c):
    if not c.isalnum():
        return ''
    if c.isdigit():
        return c

    index = LETTERS.index(c)
    return LETTERS[25 - index]


def convert(text):
    return ''.join([code(i) for i in text])


def encode(text):
    converted = convert(text.lower())
    return ' '.join([converted[i:i+5] for i in range(0, len(converted), 5)])


def decode(text):
    return convert(text.lower())

