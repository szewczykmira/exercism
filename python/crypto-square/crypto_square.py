from math import ceil, sqrt

def encode(word):
    word = ''.join(filter(lambda x: x.isalnum(), word.lower()))
    columns = ceil(sqrt(len(word)))
    return ' '.join([word[n::columns] for n in range(0, columns)])

