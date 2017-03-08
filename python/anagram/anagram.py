from collections import Counter


def detect_anagrams(word, list_of_words):
    word = word.lower()
    word_counter = Counter(word)
    C = lambda x: Counter(x.lower())
    return [x for x in list_of_words 
            if not x.lower() == word and C(x) == word_counter]
