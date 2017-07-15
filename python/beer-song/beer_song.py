VERSE_1 = '{num} bottle{pl} of beer on the wall, {num} bottle{pl} of beer.\n'
VERSE_2 = 'Take {many} down and pass it around, {smaller} bottle{pl2} of beer on the wall.\n'

SINGULAR = ''
PLURAL = 's'
ZERO = 'no more'

def number(n):
    if n == 0:
        return 'no more'
    return str(n)


def verse(num):
    pl = SINGULAR if num == 1 else PLURAL
    pl2 = SINGULAR if num == 2 else PLURAL
    many = 'it' if num == 1 else 'one'
    verse_1 = VERSE_1.format(num=number(num), pl=pl).capitalize()
    verse_2 = VERSE_2.format(smaller=number(num-1), pl2=pl2, many=many)
    if num == 0:
        verse_2 = 'Go to the store and buy some more, 99 bottles of beer on the wall.\n'
    return verse_1 + verse_2


def song(n, m=0):
    song = [verse(num) for num in range(n, m - 1, -1)]
    result = '\n'.join(song)
    return result + '\n'
