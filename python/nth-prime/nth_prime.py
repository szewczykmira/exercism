from math import sqrt

def nth_prime(n):
    if not n:
        raise ValueError
    primes = Prime()
    primes.make(n)
    return primes.primes[n-1]


class Prime:
    def __init__(self):
        self.primes = [2]

    def is_prime(self, elem):
        elem_sqrt = sqrt(elem)
        it = 0
        while self.primes[it] <= elem_sqrt:
            prime = self.primes[it]
            if not prime == elem and elem % prime == 0:
                return False
            it += 1
        return True

    def prime(self):
        last_elem = self.primes[-1] + 1
        while not self.is_prime(last_elem):
            last_elem += 1
        self.primes.append(last_elem)
        return last_elem

    def make(self, n):
        for _ in range(0, n+1):
            self.prime()

