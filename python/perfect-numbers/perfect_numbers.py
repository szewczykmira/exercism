def factors(n):
    half = int(n/2) + 1
    result = set([1])
    for i in range(2, half):
        if n % i == 0:
            result.update([i, n//i])
    return result

def is_perfect(n):
    gen = factors(n)
    sum_divisor = sum(gen)
    return sum_divisor == n
