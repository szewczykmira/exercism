NUMS = {
        1: 'first',
        2: 'second',
        3: 'third',
        4: 'fourth',
        5: 'fifth',
        6: 'sixth',
        7: 'seventh',
        8: 'eighth',
        9: 'ninth',
        10: 'tenth',
        11: 'eleventh',
        12: 'twelfth'}


GIFTS = ['a Partridge in a Pear Tree', 'two Turtle Doves',  
        'three French Hens', 'four Calling Birds', 'five Gold Rings', 
        'six Geese-a-Laying', 'seven Swans-a-Swimming',
        'eight Maids-a-Milking', 'nine Ladies Dancing', 
        'ten Lords-a-Leaping', 'eleven Pipers Piping',
        'twelve Drummers Drumming']

VERSE = 'On the {} day of Christmas my true love gave to me, {}.\n'


def gifts(n):
    if n == 1:
        return GIFTS[0]
    elems = ', '.join(GIFTS[n-1:0:-1])
    return ', and '.join([elems, GIFTS[0]])

def verse(n):
    return VERSE.format(NUMS[n], gifts(n))


def verses(begin, end):
    return '\n'.join([verse(i) for i in range(begin, end+1)]) + '\n'


def sing():
    return verses(1, 12) 
