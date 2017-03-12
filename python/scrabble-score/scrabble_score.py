LAZY_SCORES = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z']}

# Code copied from one of the previous assigment:
def transform(old_dict):
    new_dict = {}
    for key, values in old_dict.items():
        for value in values:
            new_dict.update({value.lower(): key})
    return new_dict

SOCRES = transform(LAZY_SCORES)

def score(word):
    if not word.isalpha():
        return 0
    return sum(SOCRES.get(letter.lower(), 0) for letter in word)
