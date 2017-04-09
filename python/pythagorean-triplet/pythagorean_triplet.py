from math import gcd


def primitive_triplets(num):
    """Finds all primative triplets that contain a certain number"""
    if num % 4 != 0:
        raise ValueError
    triplets = set()
    for (m, n) in factor_gen(num//2):
        if gcd(m, n) == 1:
            triplet = tuple(sorted((m**2 - n**2, 2*m*n, m**2 + n**2)))
            triplets.add(triplet)
    return triplets


def factor_gen(n):
    """Generates factor pairs of number n"""
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            yield (n//i, i)


def triplets_in_range(start, stop):
    """Generates all triplets with elements in a range"""
    triples = set()
    for c in range(start, stop+1):
        for b in range(start, c):
            for a in range(start, b):
                if a**2 + b**2 == c**2:
                    triples.add((a, b, c),)
    return triples

def is_pitagorean(a, b, c):
    return a**2 + b**2 == c**2

def is_triplet(nums):
    """Is true if nums is a primative triplet"""
    (a, b, c) = sorted(nums)
    return is_pitagorean(a, b, c) and gcd(gcd(a, b), c) == 1

