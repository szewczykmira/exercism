from operator import mul
from functools import reduce

def largest_product(string, length):
    if length < 0:
        raise ValueError
    max_range = len(string) - length + 1
    partial = [string[i:i + length] for i in range(0, max_range)]
    options = map(lambda x: [int(i) for i in x], partial)
    products = map(lambda x: reduce(mul, x, 1), options)
    return max(products)
