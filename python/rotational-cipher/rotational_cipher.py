import string

LETTERS = string.ascii_letters


def rotate_elem(elem, times):
    if elem.isalpha():
        is_lower = elem.islower()
        index = LETTERS.index(elem.lower())
        rotated_index = (index + times) % 26
        rotated_elem = LETTERS[rotated_index]
        return rotated_elem if is_lower else rotated_elem.upper()
    return elem


def rotate(word, times):
    return ''.join(rotate_elem(elem, times) for elem in word)
