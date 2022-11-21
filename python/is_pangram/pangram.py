from string import ascii_lowercase

def is_pangram(word):
    lower = set(ascii_lowercase)
    return lower.issubset(set(word.lower()))
    


assert not is_pangram("")
assert is_pangram("abcdefghijklmnopqrstuvwxyz")
assert is_pangram("the quick brown fox jumps over the lazy dog")
assert not is_pangram("a quick movement of the enemy will jeopardize five gunboats")
assert not is_pangram("five boxing wizards jump quickly at it")
assert is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog")
assert is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs")

assert not is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog")
assert is_pangram('"Five quacking Zephyrs jolt my wax bed."')
assert not is_pangram("abcdefghijklm ABCDEFGHIJKLM")
assert not is_pangram("bcdefghijklmnopqrstuvwxyz")
assert not is_pangram("abcdefghijklmnopqrstuvwxy")