from operator import add, sub, mul, truediv

PLUS = 'plus'
MINUS = 'minus'
MULTIPLY = 'multiplied by'
DIVIDED = 'divided by'
OPERATORS = [PLUS, MINUS, MULTIPLY, DIVIDED]
OPERATIONS = {PLUS: add, MINUS: sub, MULTIPLY: mul, DIVIDED: truediv}


def prepare(text):
    if not text.startswith('What is'):
        raise ValueError
        
    return text.replace('What is ', '').replace('?', '')


def split_by(text, operator):
    return [elem.strip() for elem in text.split(operator)]


def evaluate(text, operator):
    values = split_by(text, operator)
    values = [int(value) for value in values]
    operation = OPERATIONS[operator]
    return operation(*values)


def calculate(text):
    text = prepare(text)

    for operator in OPERATORS:
        if operator in text:
            return evaluate(text, operator)
    raise ValueError

