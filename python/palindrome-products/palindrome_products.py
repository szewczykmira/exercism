from collections import namedtuple


Products = namedtuple('Products', ['factors', 'product'])

def all_combinations(first, last):
    return [(i, j) for i in range(first, last+1) for j in range(first, last+1)]


def generate_products(factors_list):
    result = []
    for elem in factors_list:
        i, j = elem
        product = i*j
        if is_palindrome(product):
            result.append(Products(elem, product))
    return result


def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]


def largest_palindrome(max_factor, min_factor=1):
    products = generate_products(all_combinations(min_factor, max_factor))
    max_product = max(products, key=lambda x: x.product)
    return max_product.product, max_product.factors


def smallest_palindrome(max_factor, min_factor=1):
    products = generate_products(all_combinations(min_factor, max_factor))
    min_product = min(products, key=lambda x: x.product)
    return min_product.product, min_product.factors

