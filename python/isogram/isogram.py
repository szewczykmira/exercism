from collections import Counter

def is_isogram(word):
    word = ''.join(s for s in filter(lambda x: x.isalpha(), word))
    counter = Counter(word.lower())
    return not counter.most_common() or counter.most_common()[0][1] == 1

