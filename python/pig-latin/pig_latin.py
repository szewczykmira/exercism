VOWELS = ['a', 'e', 'i', 'o', 'u']

CLUSTERS = ['yt', 'xr']

def translate_word(word):
    while word[0] not in VOWELS and not any(
            [word.startswith(x) for x in CLUSTERS]):
        if word.startswith('qu'):
            word = word[2:] + 'qu'
        else:
            word = word[1:] + word[0]
    return word + 'ay'

def translate(phrase):
    words = phrase.split(' ')
    return ' '.join(map(translate_word, words))

