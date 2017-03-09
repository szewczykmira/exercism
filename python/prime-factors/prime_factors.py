def prime_factors(num):
    factor = 2
    factors = []
    while factor ** 2 <= num:
        if num % factor:
            factor += 1
        else:
            factors.append(factor)
            num //= factor
    if num > 1:
        factors.append(num)
    return factors
