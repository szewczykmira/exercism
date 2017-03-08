from math import pow

def square_of_sum(num):
    sum_of_n = sum(n for n in range(1, num+1))
    return pow(sum_of_n, 2)

def sum_of_squares(num):
    return sum(pow(n, 2) for n in range(1, num+1))

def difference(num):
    square_of = square_of_sum(num)
    sum_of = sum_of_squares(num)
    return abs(square_of - sum_of)
