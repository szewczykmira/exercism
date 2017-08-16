ALLOWED = ['(', ')', '[', ']', '{', '}']

CLOSURE = {
    '{': '}',
    '[': ']',
    '(': ')'
    }

def remove_not_allowed(text):
    return [i for i in text if i in ALLOWED]


def find_closure(text, elem):
    index = None
    for i, c in enumerate(text):
        if index is not None and c in CLOSURE.keys():
            return index
        if c == elem:
            index = i
    return index


def validate_brackets(text):
    if not text:
        return True

    first_elem = text[0]
    closure_index = find_closure(text, CLOSURE[first_elem])
    if not closure_index:
        raise KeyError
    first_half = validate_brackets(text[1:closure_index])
    second_half = validate_brackets(text[closure_index +1:])
    return first_half and second_half


def check_brackets(text):
    text = remove_not_allowed(text)
    try:
        return validate_brackets(text)
    except KeyError:
        return False

