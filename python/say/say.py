from collections import namedtuple

InWords = namedtuple('InWords', ['unit', 'teens', 'decimal'])

IN_WORDS = {
    1: InWords('one', 'eleven', 'ten'),
    2: InWords('two', 'twelve', 'twenty'),
    3: InWords('three', 'thirteen', 'thirty'),
    4: InWords('four', 'fourteen', 'forty'),
    5: InWords('five', 'fifteen', 'fifty'),
    6: InWords('six', 'sixteen', 'sixty'),
    7: InWords('seven', 'seventeen', 'seventy'),
    8: InWords('eight', 'eighteen', 'eighty'),
    9: InWords('nine', 'nineteen', 'ninety')
}

THOUSANDS = ['', 'thousand', 'million', 'billion']

def remove_zero(func):
    def func_wrapper(number):
        if number == 0:
            return ''
        return func(number)
    return func_wrapper


@remove_zero
def parse_hundreds(number):
    return parse_unit(number) + ' hundred'


def parse_unit(number):
    return IN_WORDS[number].unit

@remove_zero
def parse_decimal(number):
    if number < 10:
        return parse_unit(number)
    if 10 < number < 20:
        return IN_WORDS[number % 10].teens
    if number % 10 == 0:
        return IN_WORDS[number // 10].decimal
    return '{}-{}'.format(
            IN_WORDS[number // 10].decimal, parse_unit(number % 10))


@remove_zero
def hundreds(number):
    hundred = parse_hundreds(number // 100)
    decimal = parse_decimal(number % 100)
    if hundred and decimal:
        hundred += ' and '
    return '{}{}'.format(hundred, decimal)

def is_valid(number):
    if not 0 <= number < 1e12:
        raise AttributeError


def split_number(number):
    split = []
    while number >= 1000:
        split.append(number % 1000)
        number //= 1000
    split.append(number)
    return split

def say(number):
    is_valid(number)
    if number == 0:
        return 'zero'
    partial_zip = zip(map(hundreds, split_number(number)), THOUSANDS)
    partial = list(filter(lambda x: x[0], partial_zip))[::-1]
    in_words = map(lambda x: '{} {}'.format(x[0], x[1]), partial)
    return ' '.join(in_words).strip()

