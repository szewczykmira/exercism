def square(sq):
    if sq > 0 and sq < 65:
        return 2 ** (sq-1)
    raise ValueError("Mesage")

def total():
    return sum([square(n) for n in range(1, 65)])