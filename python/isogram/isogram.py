from collections import Counter

def is_isogram(word):
    word = [s.lower() for s in word if s.isalpha()]
    counter = Counter(word)
    match counter.most_common(1):
        case []:
            return True
        case [(x, 1)]:
            return True
        case _:
            return False

